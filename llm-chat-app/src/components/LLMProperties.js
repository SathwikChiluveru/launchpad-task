import { Card, Text, Button, TextInput } from '@mantine/core';
import { useState } from 'react';

export default function LLMProperties() {
  const [model, setModel] = useState('gpt-3-turbo');
  const [temperature, setTemperature] = useState(0.7);

  const handleUpdate = () => {
    console.log('Updated properties:', { model, temperature });
  };

  return (
    <Card shadow="sm" padding="lg" style={{ marginBottom: '20px' }}>
      <Text>Model: {model}</Text>
      <TextInput
        label="Update Model"
        value={model}
        onChange={(e) => setModel(e.target.value)}
      />
      <TextInput
        label="Temperature"
        type="number"
        value={temperature}
        onChange={(e) => setTemperature(parseFloat(e.target.value))}
        step="0.1"
        min="0"
        max="1"
      />
      <Button onClick={handleUpdate} style={{ marginTop: '10px' }}>
        Update Properties
      </Button>
    </Card>
  );
}
