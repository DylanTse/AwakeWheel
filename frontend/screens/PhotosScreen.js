// Screen2.js
import * as React from 'react';
import host from '../../config';
import { StyleSheet, View, Text, Dimensions } from 'react-native';

const NUM_COLUMNS = 3;
const WINDOW_WIDTH = Dimensions.get('window').width;
const COLUMN_WIDTH = WINDOW_WIDTH / NUM_COLUMNS;

export default function Screen2() {
  
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async() => {
    try {
      const response = await fetch(host + '/get_photos');
      if(!response.ok) {
        throw new Error('Failed to fetch photos');
      }
      const data = await response.json();
      setPhotos(data);
    }
    catch (error) {
      console.error('Error fetching photos: ', error);
    }
  };

  const renderPhotoItem = ({item}) => (
    <View style={styles.photoContainer}>
      <Image source={{ uri: item.imageUrl }} style={styles.photo} />
    </View>
  )

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
