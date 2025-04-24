import './global.css';
import 'katex/dist/katex.css';
import { RootProvider } from 'fumadocs-ui/provider';
import { Inter } from 'next/font/google';
import type { ReactNode } from 'react';

const inter = Inter({
  subsets: ['latin'],
});

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" className={inter.className} suppressHydrationWarning>
      <head>
        <title>The CIRIS Covenant</title>
        <meta name="description" content="CIRIS 1.0-β is a provisional, work-in-progress specification. Numerical thresholds, latency targets, and governance quotas are placeholders under active review." />
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body className="flex flex-col min-h-screen">
        <RootProvider
          search={{
            options: {
              type: 'static',
            },
          }}>
            {children}
        </RootProvider>
      </body>
    </html>
  );
}
