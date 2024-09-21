import ChatWindow from '../components/ChatWindow';
import LLMProperties from '../components/LLMProperties';

export default function Home() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>LLM Chat Interface</h1>
      <LLMProperties />
      <ChatWindow />
    </div>
  );
}
