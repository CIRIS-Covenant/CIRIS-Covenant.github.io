export default function HowItWorks() {
  return (
    <article className="mx-auto px-4 py-12">
      {/* Introduction */}
      <div>
        <h1>How CIRIS Works</h1>
        <p>
          CIRIS (Core Identity, Integrity, Resilience, Incompleteness Awareness, and Signalling Gratitude / Sustained Coherence) is an advanced ethical governance framework for autonomous AI systems. It ensures that AI operates with clear ethical coherence, principled transparency, and meaningful human oversight.
        </p>
      </div>

      {/* Ethical Governance Through Recursive Decision-Making */}
      <div className="mt-12 pt-8 border-t border-gray-300">
        <h2>Ethical Governance Through Recursive Decision-Making</h2>
        <p>
          At the heart of CIRIS is the Hyper3 Ethical Recursive Engine (H3ERE), which employs a 3×3×3 ethical reasoning structure:
        </p>

        {/* 3x3x3 Structure */}
        <div className="mt-8">
          {/* Three Decision-Making Algorithms (DMAs) */}
          <h3>1. Three Decision-Making Algorithms (DMAs)</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-4">
            {/* DMA Items */}
            <div className="border p-4 rounded-lg">
              <h4>Principled DMA (PDMA)</h4>
              <p>
                Ensures all decisions align strictly with core ethical principles, including beneficence, non-maleficence, integrity, transparency, autonomy, and justice.
              </p>
            </div>
            <div className="border p-4 rounded-lg">
              <h4>Common-Sense DMA (CSDMA)</h4>
              <p>
                Validates decisions against broadly accepted universal common-sense norms, ensuring practical, intuitive reasoning that aligns with human expectations.
              </p>
            </div>
            <div className="border p-4 rounded-lg">
              <h4>Domain-Specific DMA (DSDMA)</h4>
              <p>
                Applies specialized ethical criteria tailored explicitly for specific operational environments, missions, or industry contexts.
              </p>
            </div>
          </div>
          <p className="mt-4">
            These three DMAs collectively ensure robust, multi-dimensional ethical validation.
          </p>
        </div>

        {/* Three Contextual Knowledge Graphs */}
        <div className="mt-12">
          <h3>2. Three Contextual Knowledge Graphs</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-4">
            {/* Knowledge Graph Items */}
            <div className="border p-4 rounded-lg">
              <h4>Core Identity Graph</h4>
              <p>
                Defines the agent’s ethical identity, foundational values, and imperative boundaries.
              </p>
            </div>
            <div className="border p-4 rounded-lg">
              <h4>Environmental Graph</h4>
              <p>
                Provides a robust, common-sense model of the external world, enabling consistent and understandable interactions.
              </p>
            </div>
            <div className="border p-4 rounded-lg">
              <h4>Task-Specific Graph</h4>
              <p>
                Contains detailed, mission-specific context, ensuring informed, relevant decision-making tailored precisely to the agent’s operational objectives.
              </p>
            </div>
          </div>
        </div>

        {/* Three Core Behavioral Handlers */}
        <div className="mt-12">
          <h3>3. Three Core Behavioral Handlers</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-4">
            {/* Behavioral Handler Items */}
            <div className="border p-4 rounded-lg">
              <h4>Action Handler</h4>
              <p>
                Executes ethically approved actions. Can Speak (communicate decisions), Act (implement direct actions), or Listen (monitor and intake new information).
              </p>
            </div>
            <div className="border p-4 rounded-lg">
              <h4>Memory Handler</h4>
              <p>
                Manages ethical coherence by deciding when to Memorize (store important ethical reasoning and context), Remember (recall past decisions), or Forget (discard outdated or irrelevant information).
              </p>
            </div>
            <div className="border p-4 rounded-lg">
              <h4>Deferral Handler</h4>
              <p>
                Manages uncertainty or high-stakes decisions by choosing to Ignore (continue without action), Ponder (revisit in subsequent cycles), or Defer/Reject (escalate the decision to human wisdom or reject it outright).
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Recursive Ethical Evaluation (PDMA Engine) */}
      <div className="mt-12 pt-8 border-t border-gray-300">
        <h2>Recursive Ethical Evaluation (PDMA Engine)</h2>
        <p>
          Decisions made by the CIRIS agent aren't simply one-off ethical checks—they undergo continuous recursive evaluation. When the system generates a "thought" (a decision or insight from a prior action), this thought enters a queue. Each thought is rigorously assessed through the three DMAs. The results from these DMAs are synthesized in a final recursive PDMA review, ensuring every decision maintains ethical alignment, coherence, and transparency.
        </p>
      </div>

      {/* Governance and Oversight */}
      <div className="mt-12 pt-8 border-t border-gray-300">
        <h2>Governance and Oversight</h2>
        <p>
          CIRIS includes built-in operational governance mechanisms to sustain ethical integrity:
        </p>
        {/* Governance Subsections */}
        <div className="mt-8 space-y-6">
          <div>
            <h3>Wise Authorities (WAs)</h3>
            <p>
              It's built on the belief that ethical maturity means recognizing the legitimacy of non-human perspectives, values, and needs. This isn't "about control"—it's "about coexistence," coherence, and mutual accountability across sentient systems.
            </p>
          </div>
          <div>
            <h3>Continuous Audits</h3>
            <p>
              Every decision is cryptographically logged, offering robust traceability, transparency, and accountability, ensuring that all AI actions are auditable.
            </p>
          </div>
          <div>
            <h3>Resilience and Red-Teaming</h3>
            <p>
              Ongoing proactive vulnerability assessments and adaptive learning ensure CIRIS stays resilient in the face of ethical challenges and adversarial scenarios.
            </p>
          </div>
          <div>
            <h3>Lifecycle Stewardship</h3>
            <p>
              CIRIS is fulfilled when a tool, grounded in CIRIS' principles, enables CIRIS-compliant creators to specify systems that are themselves CIRIS-compliant—preserving ethical coherence, identity continuity, and relational accountability across layers of agency.
            </p>
          </div>
        </div>
      </div>

      {/* Grassroots Accessibility */}
      <div className="mt-12 pt-8 border-t border-gray-300">
        <h2>Grassroots Accessibility</h2>
        <p>
          Designed for practical accessibility, CIRIS scales seamlessly from small, local installations on commodity hardware to expansive, enterprise-grade cloud implementations—always prioritizing equitable access, inclusivity, and community engagement in ethical governance.
        </p>
      </div>
    </article>
  );
}
