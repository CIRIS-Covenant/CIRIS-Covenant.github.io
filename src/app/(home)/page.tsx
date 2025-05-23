import Link from 'next/link';
import Image from 'next/image';

export default function HomePage() {
  return (
    <section className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8 text-center">
        <Image src="/logo.svg" alt="CIRIS.ai Logo" width={200} height={200} className="mx-auto h-50 w-auto" />
        <h1 className="text-3xl font-extrabold text-gray-900">
          Ethics at the Core, Not the Periphery
        </h1>
        <p className="mt-2 text-sm text-gray-600">
          CIRIS.ai balances autonomous AI decision-making with meaningful human oversight, delivering resilient, transparent ethical intelligence for critical systems.
        </p>
        <div className="flex flex-col sm:flex-row justify-center gap-3">
          <Link href="/sections/main" className="btn-primary">Read the Covenant</Link>
          <Link href="/how-it-works"  className="btn-secondary">See&thinsp;How&thinsp;it&thinsp;Works</Link>
        </div>
      </div>
    </section>
  );
}
