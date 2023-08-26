/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./medicSearch/**/*.{html,js}"],
  theme: {
    extend: { 
      fontFamily: {
      inter: ['Inter', 'sans'],
      },
      colors: {
        'bgPrimary': {
        200: 'rgba(141, 174, 242, 0.71)',
        900: '#8DAEF2',
        },
        'shadowPrimary': {
        900: 'rgba(136, 163, 220, 1)',
        },
      },
  },
  plugins: [],
}
}