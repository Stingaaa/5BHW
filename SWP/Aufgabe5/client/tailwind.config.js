/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{html,js,vue}",
    './pages/**/*.{html,js}',
    '.src/components/**/*.{html,js,vue}',],
    theme: {
      extend: {},
      screens: {
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      }
    },
    plugins: [],
  }