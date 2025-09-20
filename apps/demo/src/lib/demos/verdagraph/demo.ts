import type { Demo } from '../types';
import Verdagraph from './Verdagraph.svelte';
import seed from './seed';

export const verdagraphDemo: Demo = {
	id: 'verdagraph',
	title: 'Verdagraph',
	description: 'The verdagraph allows editing plants.',
	component: Verdagraph,
	seed: seed
};
