import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, SafeAreaView, useWindowDimensions } from 'react-native';
import { GiftedChat } from 'react-native-gifted-chat'
import { useState, useCallback, useEffect } from 'react';
export default function App() {
  const [messages, setMessages] = useState([]);
  const styles = useAppStyles();
  useEffect(() => {
    setMessages([
      {
        _id: 1,
        text: 'Hello developer',
        createdAt: new Date(),
        user: {
          _id: 2,
          name: 'React Native',
          avatar: 'https://avatars.githubusercontent.com/u/14957082?s=200&v=4',
        },
      },
    ])
  }, [])

  const onSend = useCallback((messages = []) => {
    setMessages(previousMessages => GiftedChat.append(previousMessages, messages))
  }, [])

  return (
    <SafeAreaView style={styles.container}>
      <GiftedChat
        messages={messages}
        inverted={true}
        onSend={messages => onSend(messages)}
        user={{
          _id: 1,
        }}
        style={styles.chat}
      />
    </SafeAreaView>
  );
}

const useAppStyles = () => {
  const { width, height } = useWindowDimensions();
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      // backgroundColor: '#fff',
      // alignItems: 'center',
      // justifyContent: 'center',
      // height: height,
      width: width
    },
    chat: {
    }
  });
  return styles;  
}
