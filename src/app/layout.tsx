import './global.css';
import 'katex/dist/katex.css';
import { RootProvider } from 'fumadocs-ui/provider';
import { Inter, Montserrat, Open_Sans, Fira_Code } from 'next/font/google';
import Link from 'next/link';
import type { ReactNode } from 'react';

const inter = Inter({
  subsets: ['latin'],
});

const montserrat = Montserrat({
  subsets: ['latin'],
  variable: '--font-montserrat',
});

const openSans = Open_Sans({
  subsets: ['latin'],
  variable: '--font-open-sans',
});

const firaCode = Fira_Code({
  subsets: ['latin'],
  variable: '--font-fira-code',
});

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <html
      lang="en"
      className={`${inter.className} ${montserrat.variable} ${openSans.variable} ${firaCode.variable}`}
      suppressHydrationWarning
      data-theme="light"
    >
      <head>
        <title>The CIRIS Covenant</title>
        <meta name="description" content="CIRIS 1.0-β is a provisional, work-in-progress specification. Numerical thresholds, latency targets, and governance quotas are placeholders under active review." />
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body className="flex flex-col min-h-screen">
        <header className="bg-white shadow-md">
          <nav className="container mx-auto px-6 py-3">
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <img src="/logo.svg" alt="CIRIS.ai Logo" className="h-8 w-auto mr-2" />
                <Link href="/" className="text-xl font-semibold text-gray-700">CIRIS.ai&nbsp;L3C</Link>
              </div>
              <div className="flex items-center space-x-4">
                <Link href="/" className="text-gray-700 hover:text-blue-500">Home</Link>
                <Link href="/how-it-works" className="text-gray-700 hover:text-blue-500">How-it-Works</Link>
                <Link href="/about" className="text-gray-700 hover:text-blue-500">About-Us</Link>
                <Link href="/links" className="text-gray-700 hover:text-blue-500">Links/Donate</Link>
                <Link href="/sections/main" className="text-gray-700 hover:text-blue-500">Read-the-Covenant</Link>
              </div>
            </div>
          </nav>
        </header>
        <RootProvider
          search={{
            options: {
              type: 'static',
            },
          }}>
            {children}
        </RootProvider>
        <footer className="bg-gray-100 text-center py-4 mt-auto">
          <p className="text-sm text-gray-600">&copy; 2025 CIRIS.ai — Ethical Foundation for Autonomous Intelligence.</p>
        </footer>
      </body>
    </html>
  );
}
