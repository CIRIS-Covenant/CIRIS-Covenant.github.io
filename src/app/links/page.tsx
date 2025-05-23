export default function Links() {
  return (
    <section className="max-w-xl mx-auto px-4 py-12 text-center">
      <h1 className="text-2xl font-bold mb-6">Get&nbsp;Involved</h1>
      <div className="flex flex-col gap-4">
        <a href="https://github.com/CIRISAI" target="_blank" className="btn-secondary">
          🛠️&nbsp;Browse the Code
        </a>
        <a href="https://discord.gg/UuA7WvZF" target="_blank" className="btn-secondary">
          💬&nbsp;Join&nbsp;Discord
        </a>
        <a href="https://buy.stripe.com/eVa29gddk7mpaGI4gg" target="_blank" className="btn-primary">
          ❤️&nbsp;Donate via&nbsp;Stripe
        </a>
      </div>
    </section>
  );
}
