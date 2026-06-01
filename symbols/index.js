// Aggregates every icon module into a single ordered list.
// Each icon lives in its own file (e.g. ./resistor.js) and exports a default
// object: { name, category, svg }.
import switchClosed from './switch-closed.js';
import switchOpen from './switch-open.js';
import cell from './cell.js';
import battery from './battery.js';
import resistor from './resistor.js';
import capacitor from './capacitor.js';
import inductor from './inductor.js';
import wire from './wire.js';
import fuse from './fuse.js';
import variableResistor from './variable-resistor.js';
import thermistor from './thermistor.js';
import ammeter from './ammeter.js';
import voltmeter from './voltmeter.js';
import motor from './motor.js';
import diode from './diode.js';
import ldr from './ldr.js';
import ground from './ground.js';
import buzzer from './buzzer.js';
import lamp from './lamp.js';
import transistor from './transistor.js';
import and from './and.js';
import or from './or.js';
import not from './not.js';
import nand from './nand.js';
import nor from './nor.js';
import xor from './xor.js';
import xnor from './xnor.js';

export default [
  switchClosed, switchOpen, cell, battery, resistor, capacitor, inductor, wire,
  fuse, variableResistor, thermistor, ammeter, voltmeter, motor, diode, ldr,
  ground, buzzer, lamp, transistor,
  and, or, not, nand, nor, xor, xnor
];
