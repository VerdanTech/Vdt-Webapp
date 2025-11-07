import { seed } from '$lib/seeds';

import type { Demo } from '../types';
import Verdagraph from './Verdagraph.svelte';

export const verdagraphDemo: Demo = {
	id: 'verdagraph',
	title: 'Verdagraph',
	description: 'The verdagraph allows editing plants.',
	component: Verdagraph,
	seed: seed
};
