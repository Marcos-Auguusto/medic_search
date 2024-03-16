/** @type {import('tailwindcss').Config} */
module.exports = {
  plugins: [
    require('tailwindcss-animated'),
  ],
  mode: 'jit',
  content: ['./medicSearch/**/*.{html,js}', './node_modules/flowbite/**/*.js'],
  theme: {
    extend: {
      screens: {
        'ipad-pro': { raw: '(min-width: 1024px) and (max-width: 1280px)' },
      },
      spacing: {
        527: '527px',
        507: '507px',
      },
      fontFamily: {
        inter: ['Inter', 'sans'],
      },
      colors: {
        bgPrimary: {
          50: 'rgba(5, 97, 218)',
          200: 'rgba(141, 174, 242, 0.71)',
          900: '#8DAEF2',
        },
        colorBlue: {
          100: '#056cf2',
        },
        btn: {
          100: '#056cf2',
          200: '#0451B6',
          300: '#022655',
        },
        'btn-light': {
          100: '#e6f0fe',
          200: '#dae9fd',
          300: '#b2d1fb',
          500: '#86B5F6',
        },
        shadowPrimary: {
          900: 'rgba(136, 163, 220, 1)',
        },
        // rotate: {
        // '180': '180deg',
        // },
      },
    },
  },
};
