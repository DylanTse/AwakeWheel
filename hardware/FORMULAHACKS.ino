#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include "esp_camera.h"
#include <ArduinoJson.h>
#include "Base64.h"

#define CAMERA_MODEL_AI_THINKER
#include "camera_pins.h"

const char* AtlasAPIEndpoint = "HIDDEN";
const char* AtlasAPIKey = "HIDDEN";
const char* ssid = "HIDDEN";
const char* password = "HIDDEN";

int docID;

void configCamera(){
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_VGA;
  config.jpeg_quality = 12;  //0-63 lower number means higher quality
  config.fb_count = 1;

  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    delay(1000);
    ESP.restart();
  }

  // Assume USB port on top
  sensor_t * s = esp_camera_sensor_get();
  s->set_saturation(s,2);
  s->set_vflip(s, 1);
  s->set_hmirror(s, 1);
}

void setup() {
  configCamera();
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  WiFi.begin(ssid, password);
  WiFi.setSleep(false);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println();
  Serial.print("ESP32-CAM IP Address: ");
  Serial.println(WiFi.localIP());
}


void loop() {
  camera_fb_t * fb = NULL;
  fb = esp_camera_fb_get();

  if (!fb) {
    Serial.println("Camera capture failed");
    delay(1000);
    ESP.restart();
  }
  Serial.println("Picture:");
  String base64Image = base64::encode(fb->buf, fb->len);
  Serial.println(base64Image);
  mongoRun(base64Image);
  esp_camera_fb_return(fb);
  delay(1000);
}

void mongoRun(String base64Image) {      
      HTTPClient https;
      if (https.begin(AtlasAPIEndpoint)) {
        https.addHeader("Content-Type", "application/json");
        https.addHeader("Access-Control-Request-Headers", "*");
        https.addHeader("api-key", AtlasAPIKey);
      
        DynamicJsonDocument payload (1024);
        JsonObject root = payload.to<JsonObject>();
        root["collection"] = "Pictures";
        root["database"] = "MainDB";
        root["dataSource"] = "Cluster0";

        JsonObject document = root.createNestedObject("document");
        document["_id"] = String(docID);
        ++docID;
        document["base64Image"] = base64Image;
        
        String JSONText;
        serializeJson(payload, JSONText);
        int httpCode = https.POST(JSONText);
        if (httpCode > 0) {
          String response = https.getString();
          Serial.println(response);
        } 
        else {
          Serial.println("HTTP Request Error");
        }
      }
      https.end();
}