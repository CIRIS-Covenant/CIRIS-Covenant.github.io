# ciris

This is a Next.js application generated with
[Create Fumadocs](https://github.com/fuma-nama/fumadocs).

## Run Development Server

```bash
npm run dev
# or
pnpm dev
# or
yarn dev
```

Open http://localhost:3000 with your browser to see the result.

## Static Site Generation (SSG)

This project is configured to generate a static site using Next.js. Follow these steps to build and export the static site:

1. **Build the Project**  
   Run the following command to build the project and export it as static files:

   ```bash
   npm run build
   ```

   This will generate the static files in the `out/` directory.

2. **Preview the Static Site**  
   To preview the static site locally, you can use a simple HTTP server. For example:

   ```bash
   npx serve out
   ```

   Open http://localhost:3000 to view the static site.

3. **Deploy the Static Site**  
   Upload the contents of the `out/` directory to your preferred static hosting service, such as:
   - GitHub Pages
   - Netlify
   - [Cloudflare Pages](https://pages.cloudflare.com/)

## Learn More

To learn more about Next.js and Fumadocs, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [Fumadocs](https://fumadocs.vercel.app) - learn about Fumadocs.