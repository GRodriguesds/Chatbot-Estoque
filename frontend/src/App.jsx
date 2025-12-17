import { useState } from "react";
import { Trash2, Send } from "lucide-react";

export default function App() {
  const [mensagem, setMensagem] = useState("");
  const [respostas, setRespostas] = useState([]);
  const [loading, setLoading] = useState(false);

  const enviarMensagem = async () => {
    if (!mensagem.trim()) return;

    setLoading(true);

    setRespostas((prev) => [...prev, { role: "user", text: mensagem }]);
    setMensagem("");

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensagem })
      });

      const data = await response.json();

      setRespostas((prev) => [...prev, { role: "bot", text: data.resposta }]);
    } catch {
      setRespostas((prev) => [...prev, { role: "bot", text: "Erro ao conectar com o servidor." }]);
    } finally {
      setLoading(false);
    }
  };

  const limparChat = () => {
    setRespostas([]);
    setMensagem("");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-zinc-900 via-black to-zinc-900 flex items-center justify-center">
      <div className="w-full max-w-xl h-[85vh] bg-zinc-900/90 backdrop-blur text-white rounded-3xl shadow-2xl flex flex-col overflow-hidden border border-zinc-800">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-zinc-800">
          <h1 className="text-xl font-bold tracking-wide">Chatbot de Estoque</h1>
          <button
            onClick={limparChat}
            className="flex items-center gap-2 text-sm bg-zinc-800 hover:bg-red-600/20 hover:text-red-400 px-3 py-1.5 rounded-lg transition"
          >
            <Trash2 size={16} /> Limpar
          </button>
        </div>

        {/* Mensagens */}
        <div className="flex-1 p-6 space-y-4 overflow-y-auto">
          {respostas.length === 0 && (
            <div className="h-full flex items-center justify-center">
              <p className="text-zinc-500 text-sm">
                Pergunte sobre produtos disponíveis no estoque
              </p>
            </div>
          )}

          {respostas.map((msg, index) => (
            <div
              key={index}
              className={`max-w-[75%] px-4 py-2.5 rounded-2xl text-sm leading-relaxed shadow ${
                msg.role === "user"
                  ? "bg-blue-600 ml-auto"
                  : "bg-zinc-800"
              }`}
            >
              {msg.text}
            </div>
          ))}

          {loading && (
            <div className="bg-zinc-800 px-4 py-2 rounded-2xl text-sm w-fit animate-pulse">
              Digitando...
            </div>
          )}
        </div>

        {/* Input */}
        <div className="p-4 border-t border-zinc-800 flex gap-3">
          <input
            type="text"
            value={mensagem}
            onChange={(e) => setMensagem(e.target.value)}
            placeholder="Digite sua pergunta..."
            className="flex-1 bg-zinc-800 border border-zinc-700 rounded-2xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-blue-600"
            onKeyDown={(e) => e.key === "Enter" && enviarMensagem()}
          />
          <button
            onClick={enviarMensagem}
            className="bg-blue-600 hover:bg-blue-700 transition px-4 rounded-2xl flex items-center justify-center shadow"
          >
            <Send size={18} />
          </button>
        </div>
      </div>
    </div>
  );
}
