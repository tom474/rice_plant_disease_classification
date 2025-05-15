"use client";

import Image from "next/image";
import { useEffect, useState } from "react";
import { format } from "date-fns";
import { Button } from "@/components/ui/button";

type HistoryItem = {
  _id?: string;
  image_id: string;
  image_url: string;
  timestamp: string;
  disease: { result: string };
  variety: { result: string };
  age: { result: number };
};

const ITEMS_PER_PAGE = 8;

export default function History() {
  const [history, setHistory] = useState<HistoryItem[]>([]);
  const [currentPage, setCurrentPage] = useState(1);

  const fetchHistory = async () => {
    try {
      const res = await fetch(
        "https://rice-plant-disease-classification.k-clowd.top/api/history/"
      );
      const data = await res.json();
      setHistory(data);
    } catch (err) {
      console.error("Failed to fetch history", err);
    }
  };

  useEffect(() => {
    fetchHistory();

    const onUpdate = () => fetchHistory();
    window.addEventListener("prediction:completed", onUpdate);
    return () => window.removeEventListener("prediction:completed", onUpdate);
  }, []);

  // Pagination logic
  const totalPages = Math.ceil(history.length / ITEMS_PER_PAGE);
  const paginated = history.slice(
    (currentPage - 1) * ITEMS_PER_PAGE,
    currentPage * ITEMS_PER_PAGE
  );

  return (
    <section id="history" className="py-20 px-4 max-w-6xl mx-auto">
      <h2 className="text-3xl font-bold mb-6 text-center">
        Prediction History
      </h2>

      {paginated.length === 0 ? (
        <p className="text-muted-foreground text-center">
          No predictions recorded yet.
        </p>
      ) : (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {paginated.map((item) => (
              <div
                key={item.image_id}
                className="border rounded-lg p-4 bg-background shadow-sm space-y-2"
              >
                <Image
                  src={`https://rice-plant-disease-classification.k-clowd.top${item.image_url}`}
                  alt="Predicted image"
                  width={300}
                  height={300}
                  className="rounded w-full object-cover"
                />
                <p className="text-sm text-muted-foreground">
                  {format(new Date(item.timestamp), "yyyy-MM-dd HH:mm:ss")}
                </p>
                <p>
                  <strong>Disease:</strong> {item.disease.result}
                </p>
                <p>
                  <strong>Variety:</strong> {item.variety.result}
                </p>
                <p>
                  <strong>Age:</strong> {item.age.result} days
                </p>
              </div>
            ))}
          </div>

          {/* Pagination Controls */}
          <div className="flex justify-center gap-4 mt-10">
            <Button
              variant="outline"
              disabled={currentPage === 1}
              onClick={() => setCurrentPage((p) => p - 1)}
            >
              Previous
            </Button>
            <span className="text-sm text-muted-foreground pt-2">
              Page {currentPage} of {totalPages}
            </span>
            <Button
              variant="outline"
              disabled={currentPage === totalPages}
              onClick={() => setCurrentPage((p) => p + 1)}
            >
              Next
            </Button>
          </div>
        </>
      )}
    </section>
  );
}
