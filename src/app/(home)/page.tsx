import Link from 'next/link';

export default function HomePage() {
  return (
    <section className="bg-[#081523] min-h-screen flex">
      <main className="flex flex-1 flex-col justify-center text-center max-w-2xl mx-auto px-4">
        <img src="/cirisImg.jpg" alt="Ciris Image" className="max-w-sm mx-auto mb-8" />
        <h1 className="text-3xl font-bold text-white">The CIRIS Covenant</h1>
        <p className="text-gray-400 mt-6">
          CIRIS 1.0-β is a provisional, work-in-progress specification. Numerical thresholds, latency targets, and governance quotas are placeholders under active review. Do not build safety-critical systems that rely solely on this draft.
        </p>
        <Link href="/sections/main" className="text-white font-semibold underline mt-6">
          Read the full specification
        </Link>
        <Link href="/apply" className="text-white font-semibold underline mt-6">
          Apply to Join
        </Link>
      </main>
    </section>
  );
}
