import { useState } from 'react';
import { TextInput, Button } from '@mantine/core';

export default function PromptInput({ onSendPrompt }) {
  const [prompt, setPrompt] = useState('');

  const handleSend = () => {
    if (prompt) {
      onSendPrompt(prompt);
      setPrompt('');
    }
  };

  return (
    <div style={{ display: 'flex', marginTop: '10px' }}>
      <TextInput
        value={prompt}
        onChange={(event) => setPrompt(event.currentTarget.value)}
        placeholder="Enter your prompt"
        style={{ flexGrow: 1 }}
      />
      <Button onClick={handleSend} style={{ marginLeft: '10px' }}>
        Send
      </Button>
    </div>
  );
}
