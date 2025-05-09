import PaddyScanner from "@/components/PaddyScanner";
import History from "@/components/History";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <div className="grid grid-cols-1">
      <PaddyScanner />
      <History />
      <Footer />
    </div>
  );
}
