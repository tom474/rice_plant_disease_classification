import PaddyScanner from "@/components/PaddyScanner";
import History from "@/components/History";

export default function Home() {
  return (
    <div className="grid grid-cols-1">
      <PaddyScanner />
      <History />
    </div>
  );
}
