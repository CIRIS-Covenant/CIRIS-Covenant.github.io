import { createMDX } from 'fumadocs-mdx/next';

const withMDX = createMDX();

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
  // distDir: 'dist',
  output: 'export', // Static Site Generation
};

export default withMDX(config);
