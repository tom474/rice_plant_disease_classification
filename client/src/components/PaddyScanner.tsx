"use client";

import { useEffect, useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import Image from "next/image";
import { cn } from "@/lib/utils";

export default function PaddyScanner() {
  const [visible, setVisible] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [result, setResult] = useState<{
    age?: number;
    disease?: string;
    variety?: string;
  } | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setVisible(true), 100);
    return () => clearTimeout(timer);
  }, []);

  const handleUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = e.target.files?.[0];
    if (selected) {
      setFile(selected);
      setPreview(URL.createObjectURL(selected));
      setResult(null);
    }
  };

  const handleSubmit = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    const res = await fetch("http://localhost:8000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <section
      id="paddy-scanner"
      className={cn(
        "min-h-screen flex flex-col justify-center items-center transition-opacity duration-1000 ease-in px-4",
        visible ? "opacity-100" : "opacity-0"
      )}
    >
      {/* Logo & Headline */}
      <div className="flex flex-col items-center text-center mb-10">
        <div className="flex items-center justify-center">
          <Image
            src="/logo-sm.png"
            alt="logo"
            width={100}
            height={100}
            priority
          />
          <span className="text-3xl font-bold">PaddyScannerAI</span>
        </div>
        <h1 className="text-3xl md:text-5xl font-bold tracking-tight mt-2 md:mt-0">
          Diagnose. Detect. Predict.
        </h1>
        <p className="text-muted-foreground text-base md:text-lg mt-2 max-w-xl">
          Upload a paddy plant image to detect diseases, identify variety, and
          estimate plant age.
        </p>
      </div>

      {/* Upload + Result Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-20 w-full max-w-4xl">
        {/* Upload Column */}
        <div className="space-y-4 h-[500px] w-full max-w-md border rounded-lg p-6 bg-background shadow-sm">
          <Input type="file" accept="image/*" onChange={handleUpload} />

          <div className="flex justify-center">
            {preview && (
              <Image
                src={preview}
                alt="Uploaded preview"
                width={250}
                height={250}
                className="rounded border"
              />
            )}
          </div>

          <Button
            onClick={handleSubmit}
            disabled={loading || !file}
            className="w-full"
          >
            {loading ? "Scanning..." : "Scan Image"}
          </Button>
        </div>

        {/* Result Column */}
        <div className="text-left border rounded-lg p-6 shadow-sm">
          <h2 className="text-xl font-semibold mb-2">Prediction Result</h2>
          {/* Dummy */}
          <p>
            <strong>Disease:</strong> {result?.disease || "N/A"}
          </p>
          <p>
            <strong>Variety:</strong> {result?.variety || "N/A"}
          </p>
          <p>
            <strong>Estimated Age:</strong>{" "}
            {result?.age !== undefined ? `${result.age} days` : "N/A"}
          </p>
          {/* {!result && <p className="text-muted-foreground">Results will appear here after scanning.</p>}
          {result && (
            <div className="space-y-2 text-sm">
              {result.disease && <p><strong>Disease:</strong> {result.disease}</p>}
              {result.variety && <p><strong>Variety:</strong> {result.variety}</p>}
              {result.age !== undefined && (
                <p><strong>Estimated Age:</strong> {result.age} days</p>
              )}
            </div>
          )} */}
        </div>
      </div>
    </section>
  );
}
