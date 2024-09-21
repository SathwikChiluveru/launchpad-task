import { useState } from 'react';
import { Card, Text, Button } from '@mantine/core';
import PromptInput from './PromptInput';
import { useQueryClient } from 'react-query';
import { getConversation, sendPrompt } from '../services/api';

export default function ChatWindow() {
  const queryClient = useQueryClient();
  const [conversationId, setConversationId] = useState(null);
  const [messages, setMessages] = useState([]);

  const handleSendPrompt = async (prompt) => {
    const response = await sendPrompt(conversationId, prompt);
    setMessages([...messages, { prompt, response }]);
  };

  const handleNewConversation = async () => {
    const newConversation = await getConversation();
    setConversationId(newConversation.id);
    setMessages([]);
  };

  return (
    <Card shadow="sm" padding="lg">
      <Button onClick={handleNewConversation}>New Conversation</Button>
      {messages.map((msg, index) => (
        <Text key={index}>
          <strong>Prompt:</strong> {msg.prompt} <br />
          <strong>Response:</strong> {msg.response}
        </Text>
      ))}
      <PromptInput onSendPrompt={handleSendPrompt} />
    </Card>
  );
}
