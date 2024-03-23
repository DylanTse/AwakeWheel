import * as React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Screen1 from './StatsScreen.js';
import Screen2 from './PhotosScreen.js';

const Tab = createBottomTabNavigator();

function TabNavigator() {
  return (
    <Tab.Navigator
        screenOptions={{
            headerShown: false,
        }}>
      <Tab.Screen name="Stats" component={Screen1} />
      <Tab.Screen name="Photos" component={Screen2} />
    </Tab.Navigator>
  );
}

export default TabNavigator;
