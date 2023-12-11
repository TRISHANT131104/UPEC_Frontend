/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
      colors: {
        'title-text-color': '#5E5873',
        'title-bg-color':'#FFFFFF',
        'body-text-color':'#8D899C',
        'body-bg-color': '#FFFFFF',
        'link-text-color':'#0065C1',
        'background-bg-color':'#F7F7F7',
        'hover-bg-color':'#E9F3FF'
      },
    },
  },
  plugins: [],
}
