import type { Demo } from './types';
import { verdagraphDemo } from './verdagraph';
import { workspaceDemo } from './workspaceEditor';

export const demos: Demo[] = [verdagraphDemo, workspaceDemo];

export type DemoId = (typeof demos)[number]['id'];
