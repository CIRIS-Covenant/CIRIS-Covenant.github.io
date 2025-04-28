'use client';

import { useState } from 'react';

export default function ApplyPage() {
  // Form state
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    github: '',
    role: '',
    message: '',
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Form submit handler
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // TODO: Replace alert with POST request to backend (e.g. /api/apply)
    // fetch('/api/apply', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(formData),
    // });

    alert(`Application submitted:\n${JSON.stringify(formData, null, 2)}`);
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">Apply to access private agent code</h1>

      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
          name="name"
          placeholder="Full Name"
          required
          onChange={handleChange}
          value={formData.name}
          className="border p-2"
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          required
          onChange={handleChange}
          value={formData.email}
          className="border p-2"
        />
        <input
          type="url"
          name="github"
          placeholder="GitHub Profile URL"
          onChange={handleChange}
          value={formData.github}
          className="border p-2"
        />

        <label className="block mb-1 font-medium">Role</label>
        <select
          name="role"
          required
          onChange={handleChange}
          value={formData.role}
          className="border p-2"
          aria-label="Select your role"
        >
          <option value="">Select Role</option>
          <option value="developer">Developer</option>
          <option value="designer">Designer</option>
          <option value="qa">QA</option>
        </select>

        <textarea
          name="message"
          placeholder="How would you like to help?"
          required
          onChange={handleChange}
          value={formData.message}
          className="border p-2"
        />

        <button
          type="submit"
          className="bg-blue-600 text-white py-2 px-4 rounded"
        >
          Submit
        </button>
      </form>
    </div>
  );
}