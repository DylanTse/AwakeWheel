// Screen2.js
import * as React from 'react';
import { StyleSheet, View, Text, Dimensions } from 'react-native';

export default function Screen2() {
  
  const numColumns = 3;
  const windowWidth = Dimensions.get('window').width;
  const colWidth = windowWidth / numColumns;


  
  
  return (
    <View style={styles.container}>
        <Text style={styles.heading}>Photos</Text>
        <FlatList
          
        />
    </View>
  );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      paddingLeft: 20,
      paddingTop: 55,
    },
    heading: {
      fontSize: 40,
      paddingBottom: 20,
    },
    text: {
      fontSize: 20,
      paddingBottom: 10,
    }
  });
