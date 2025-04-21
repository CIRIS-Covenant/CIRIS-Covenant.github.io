import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import type { ReactNode } from 'react';
import { baseOptions } from '@/app/layout.config';
import { source } from '@/lib/source';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout tree={source.pageTree} {...baseOptions} sidebar={{
      tabs: [
        {
          title: 'Formula Docs',
          description: 'Formula Docs is a documentation site for CIRIS, a specification for a new standard of safety-critical systems.',
          // active for `/docs/components` and sub routes like `/docs/components/button`
          url: '/books/formula',

          // optionally, you can specify a set of urls which activates the item
          // urls: new Set(['/docs/test', '/docs/components']),
        },
      ],
    }}>
      {children}
    </DocsLayout>
  );
}
