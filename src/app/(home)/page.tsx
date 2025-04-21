import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="flex flex-1 flex-col justify-center text-center max-w-2xl mx-auto px-4">
      <h1 className="mb-4 text-3xl font-bold">The CIRIS Covenant</h1>
      <p className="text-fd-muted-foreground mt-4">
        CIRIS 1.0-β is a provisional, work-in-progress specification. Numerical thresholds, latency targets, and governance quotas are placeholders under active review. Do not build safety-critical systems that rely solely on this draft.
      </p>
      <p className="text-fd-muted-foreground mt-4">
        <Link href="/books" className="text-fd-foreground font-semibold underline">
          Read the full specification
        </Link>
      </p>
    </main>
  );
}
