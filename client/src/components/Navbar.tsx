"use client";

import { useTheme } from "next-themes";
import { usePathname } from "next/navigation";
import Image from "next/image";
import Link from "next/link";
import { Moon, Sun, Menu } from "lucide-react";
import { Button } from "./ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "./ui/dropdown-menu";
import { Sheet, SheetContent, SheetTrigger, SheetHeader } from "./ui/sheet";

// eslint-disable-next-line
const Navbar = () => {
  // eslint-disable-next-line
  const { theme, setTheme } = useTheme();
  const pathname = usePathname();

  return (
    <nav className="border-b shadow-sm px-4 py-3">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-2">
          <Image src="/logo-sm.png" alt="logo" width={40} height={40} />
          <span className="text-lg font-bold">PaddyScannerAI</span>
        </Link>

        {/* Desktop Nav */}
        <div className="hidden md:flex items-center gap-4">
          <Link
            href="#paddy-scanner"
            className={`transition-colors ${
              pathname === "/#paddy-scanner" ? "font-bold" : ""
            }`}
          >
            Paddy Scanner
          </Link>
          <Link
            href="#history"
            className={`transition-colors ${
              pathname === "/#history" ? "font-bold" : ""
            }`}
          >
            History
          </Link>

          {/* Theme Toggle */}
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="outline" size="icon">
                <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
                <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
                <span className="sr-only">Toggle theme</span>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              <DropdownMenuItem onClick={() => setTheme("light")}>
                Light
              </DropdownMenuItem>
              <DropdownMenuItem onClick={() => setTheme("dark")}>
                Dark
              </DropdownMenuItem>
              <DropdownMenuItem onClick={() => setTheme("system")}>
                System
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>

        {/* Mobile Nav (Hamburger + Sheet) */}
        <div className="md:hidden">
          <Sheet>
            <SheetTrigger asChild>
              <Button variant="ghost" size="icon">
                <Menu className="h-5 w-5" />
              </Button>
            </SheetTrigger>
            <SheetContent side="right" className="w-64">
              <SheetHeader>
                <span className="font-bold text-lg">Menu</span>
              </SheetHeader>
              <div className="ml-3 flex flex-col gap-4">
                <Link href="/#paddy-scanner" className="text-base">
                  Paddy Scanner
                </Link>
                <Link href="/#history" className="text-base">
                  History
                </Link>
                <div className="border-t pt-4">
                  <span className="block text-sm mb-1 text-muted-foreground">
                    Theme
                  </span>
                  <div className="flex gap-2">
                    <Button variant="outline" onClick={() => setTheme("light")}>
                      Light
                    </Button>
                    <Button variant="outline" onClick={() => setTheme("dark")}>
                      Dark
                    </Button>
                    <Button
                      variant="outline"
                      onClick={() => setTheme("system")}
                    >
                      System
                    </Button>
                  </div>
                </div>
              </div>
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
