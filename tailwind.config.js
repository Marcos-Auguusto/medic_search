/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    "./medicSearch/**/*.{html,js}",
    "./node_modules/flowbite/**/*.js"
  ],
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
        'colorBlue':{
          100:'#056cf2'
        },
        'btn': {
          100:'#056cf2',
          200:'#0451B6',
          300:'#022655',
        },
        'shadowPrimary': {
        900: 'rgba(136, 163, 220, 1)',
        },
      },
  },
  plugins: [
    require('flowbite/plugin')
  ]
}

}