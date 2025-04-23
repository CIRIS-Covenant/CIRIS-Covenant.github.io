import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

/**
 * Shared layout configurations
 *
 * you can customise layouts individually from:
 * Home Layout: app/(home)/layout.tsx
 * Docs Layout: app/docs/layout.tsx
 */
export const baseOptions: BaseLayoutProps = {
  nav: {
    title: (
      <>
        <img
          src="/cirisImg.jpg"
          alt="CIRIS Logo"
          width={24}
          height={24}
          className="rounded-full" // Optional: Keep the circular shape if desired
        />
        CIRIS
      </>
    ),
    url: '/sections/main', // Set the link URL here
  },
  // links: [
  //   {
  //     text: 'Sections',
  //     url: '/sections',
  //     active: 'nested-url',
  //   },
  // ],
};
