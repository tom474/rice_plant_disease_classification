"use client"

import Image from "next/image"

type HistoryItem = {
  _id: string
  imageUrl: string
  age?: number
  disease?: string
  variety?: string
  timestamp: string
}

// 🧪 MOCK DATA
const mockHistory: HistoryItem[] = Array.from({ length: 3 }, (_, i) => ({
  _id: `mock-${i}`,
  imageUrl: `/200001.jpg`,
  age: Math.floor(Math.random() * 30 + 45), // between 45–75
  disease: ["blast", "hispa", "tungro", "healthy"][Math.floor(Math.random() * 4)],
  variety: ["jasmine", "basmati", "glutinous"][Math.floor(Math.random() * 3)],
  timestamp: new Date(Date.now() - i * 86400000).toISOString(), // last 10 days
}))

export default function History() {
  // 🔒 Real data commented for now
  // const [history, setHistory] = useState<HistoryItem[]>([])
  // useEffect(() => {
  //   fetch("http://localhost:8000/history")
  //     .then(res => res.json())
  //     .then(data => setHistory(data))
  // }, [])

  const history = mockHistory

  return (
    <section id="history" className="py-20 px-4 max-w-6xl mx-auto">
      <h2 className="text-3xl font-bold mb-6 text-center">Prediction History</h2>

      {history.length === 0 ? (
        <p className="text-muted-foreground text-center">
          No predictions recorded yet.
        </p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {history.map((item) => (
            <div
              key={item._id}
              className="border rounded-lg p-4 bg-background shadow-sm space-y-2"
            >
              <Image
                src={item.imageUrl}
                alt="Predicted image"
                width={300}
                height={300}
                className="rounded w-full object-cover"
              />
              <p className="text-sm text-muted-foreground">
                {new Date(item.timestamp).toLocaleString()}
              </p>
              <p><strong>Disease:</strong> {item.disease}</p>
              <p><strong>Variety:</strong> {item.variety}</p>
              <p><strong>Age:</strong> {item.age} days</p>
            </div>
          ))}
        </div>
      )}
    </section>
  )
}
