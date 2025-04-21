import { defineDocs, defineConfig } from 'fumadocs-mdx/config';

// Options: https://fumadocs.vercel.app/docs/mdx/collections#define-docs
export const docs = defineDocs({
  dir: 'content/books',
});

export default defineConfig({
  mdxOptions: {
    // MDX options
  },
});
