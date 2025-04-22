import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';
import { defineDocs, defineConfig } from 'fumadocs-mdx/config';

// Options: https://fumadocs.vercel.app/docs/mdx/collections#define-docs
export const docs = defineDocs({
  dir: 'content/sections',
});

export default defineConfig({
  mdxOptions: {
    remarkPlugins: [remarkMath],
    // Place it at first so that it won't be changed by syntax highlighter
    rehypePlugins: (v) => [rehypeKatex, ...v],
  },
});
