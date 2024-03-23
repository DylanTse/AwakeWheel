// Screen2.js
import * as React from 'react';
import { StyleSheet, View, Text, Dimensions } from 'react-native';

export default function Screen2() {
  
  const NUM_COLUMNS = 3;
  const WINDOW_WIDTH = Dimensions.get('window').width;
  const COLUMN_WIDTH = WINDOW_WIDTH / NUM_COLUMNS;
  
  return (
    <View style={styles.container}>
        <FlatList
          data = {photos}
          keyExtractor={item => item.id.toString()}
          renderItem={renderPhotoItem}
          numColumns={NUM_COLUMNS}
          columnWrapperStyle={styles.columnWrapper}
        />
    </View>
  );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#fff',
    },
    photo: {
      width: COLUMN_WIDTH,
      height: COLUMN_WIDTH,
      margin: 2,
    },
    columnWrapper: {
      justifyContent: 'space-between',
    }
  });
