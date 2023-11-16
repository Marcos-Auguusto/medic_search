/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: ["./medicSearch/**/*.{html,js}"],
  theme: {
    extend: {
      spacing: {
        '527': '527px',
        '507': '507px',
      },       
      fontFamily: {
      inter: ['Inter', 'sans'],
      },
      colors: {
        'bgPrimary': {
        200: 'rgba(141, 174, 242, 0.71)',
        900: '#8DAEF2',
        },
        'btn': {
          200:'#0451B6',
        },
        'shadowPrimary': {
        900: 'rgba(136, 163, 220, 1)',
        },
      },
  },
  plugins: [],
  }

}