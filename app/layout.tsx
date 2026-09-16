import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "308 Digital — AI Solutions",
  description: "AI consulting for finance, insurance, healthcare, and retail",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
