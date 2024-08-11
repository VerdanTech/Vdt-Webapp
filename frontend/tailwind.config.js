/** @type {import('tailwindcss').Config} */
const config = {
	darkMode: 'selector',
	content: ['./src/**/*.{html,js,svelte,ts}'],
	plugins: [require('@tailwindcss/container-queries')],
	theme: {
		container: {
			center: true,
			padding: '2rem',
			screens: {
				'2xl': '1400px'
			}
		},
		extend: {
			/*
			 * Colors used are from Radix-UI.
			 * Note that colors used here must be imported as CSS variables
			 * within src/app.pcss
			 */
			colors: {
				neutral: getColorScale('olive'),
				primary: getColorScale('grass'),
				secondary: getColorScale('teal'),
				accent: getColorScale('cyan'),
				destructive: getColorScale('tomato'),
				warning: getColorScale('amber'),
				success: getColorScale('mint')
			}
		}
	}
}

/**
 * Generates a color scale object for Tailwind CSS with values from 1 to 12.
 * Used to alias Radix-UI colors into Tailwind colors.
 *
 * Taken from (https://fynn.at/shorts/2023-03-19-how-to-use-radix-colors-with-tailwind-css)
 *
 * @param {string} name - The base name of the color scale from Radix-UI.
 * @returns {Record<string, string>} An object representing the color scale, with keys from 1 to 12 and corresponding CSS variable values.
 */
function getColorScale(name) {
	const scale = {}
	for (let i = 1; i <= 12; i++) {
		scale[i] = `var(--${name}-${i})`
		// next line only needed if using alpha values
		//scale[`a${i}`] = `var(--${name}-a${i})`;
	}

	return scale
}

export default config
