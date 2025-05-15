"use client";

import { useTheme } from "next-themes";
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
import {
  Sheet,
  SheetContent,
  SheetTrigger,
  SheetHeader,
  SheetTitle,
  SheetDescription,
} from "./ui/sheet";
import { useState } from "react";

const Navbar = () => {
  const { theme, setTheme } = useTheme();
  const [isOpen, setIsOpen] = useState(false);

  console.log("Current theme:", theme);

  return (
    <nav className="sticky top-0 z-50 border-b shadow-sm px-4 py-3 bg-background backdrop-blur supports-[backdrop-filter]:bg-background/80">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Logo */}
        <Link
          href="/"
          className="flex items-center gap-2"
          aria-label="Go to homepage"
        >
          <Image
            src="/logo-sm.png"
            alt="logo"
            width={40}
            height={40}
            loading="lazy"
          />
          <span className="text-lg font-bold">PaddyScannerAI</span>
        </Link>

        {/* Desktop Nav */}
        <div className="hidden md:flex items-center gap-4">
          <Link href="#paddy-scanner" className="transition-colors">
            Paddy Scanner
          </Link>
          <Link href="#history" className="transition-colors">
            History
          </Link>

          {/* Theme Toggle */}
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="outline" size="icon" aria-label="Toggle theme">
                <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
                <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
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
          <Sheet open={isOpen} onOpenChange={setIsOpen}>
            <SheetTrigger asChild>
              <Button variant="ghost" size="icon" aria-label="Open menu">
                <Menu className="h-5 w-5" />
              </Button>
            </SheetTrigger>
            <SheetContent
              side="right"
              className="w-64"
              aria-describedby={undefined}
            >
              <SheetHeader>
                <SheetTitle>PaddyScannerAI</SheetTitle>
                <SheetDescription>
                  Diagnose diseases, identify variety, and predict age of rice
                  plants.
                </SheetDescription>
              </SheetHeader>

              <div className="ml-3 flex flex-col gap-4 border-t pt-4">
                <button
                  className="text-base text-left hover:underline"
                  onClick={() => {
                    setIsOpen(false);
                    setTimeout(() => {
                      document
                        .getElementById("paddy-scanner")
                        ?.scrollIntoView({ behavior: "smooth" });
                    }, 300);
                  }}
                >
                  Paddy Scanner
                </button>
                <button
                  className="text-base text-left hover:underline"
                  onClick={() => {
                    setIsOpen(false);
                    setTimeout(() => {
                      document
                        .getElementById("history")
                        ?.scrollIntoView({ behavior: "smooth" });
                    }, 300);
                  }}
                >
                  History
                </button>

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
