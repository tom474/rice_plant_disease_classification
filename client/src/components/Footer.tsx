export default function Footer() {
  return (
    <footer className="w-full border-t bg-background py-6 text-center text-sm text-muted-foreground">
      <p>© {new Date().getFullYear()} PaddyScannerAI. All rights reserved.</p>
    </footer>
  );
}
