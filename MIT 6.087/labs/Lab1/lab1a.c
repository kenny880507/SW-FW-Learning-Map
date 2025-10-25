/*
 * lab1a.c
 *
 *  Created on:
 *      Author:
 */

/* include helper functions for game */
#include "lifegame.h"

/* add whatever other includes here */

/* number of generations to evolve the world */
#define NUM_GENERATIONS 50

/* functions to implement */

/* this function should set the state of all
   the cells in the next generation and call
   finalize_evolution() to update the current
   state of the world to the next generation */
void next_generation(void);

/* this function should return the state of the cell
   at (x,y) in the next generation, according to the
   rules of Conway's Game of Life (see handout) */
int get_next_state(int x, int y);

/* this function should calculate the number of alive
   neighbors of the cell at (x,y) */
int num_neighbors(int x, int y);

int main(void)
{
	int n;

	/* TODO: initialize the world */
	initialize_world();
	output_world();
	
	for (n = 0; n < NUM_GENERATIONS; n++)
		next_generation();
		

	/* TODO: output final world state */
	output_world();

	return 0;
}

void next_generation(void) {
	/* TODO: for every cell, set the state in the next
	   generation according to the Game of Life rules

	   Hint: use get_next_state(x,y) */

	int i,j;

	for(i=0;i<get_world_width();++i){
		for(j=0;j<get_world_height();++j){
			set_cell_state(i,j,get_next_state(i,j));
		}
	}
	finalize_evolution(); /* called at end to finalize */
}

int get_next_state(int x, int y) {
	/* TODO: for the specified cell, compute the state in
	   the next generation using the rules

	   Use num_neighbors(x,y) to compute the number of live
	   neighbors */
	int state = get_cell_state(x,y);
	if(state==ALIVE){
		if(num_neighbors(x,y)>3 || num_neighbors(x,y)<2) state=DEAD;
	} else{
		if(num_neighbors(x,y)==3) state=ALIVE;
	}
	return state;
}

int num_neighbors(int x, int y) {
	/* TODO: for the specified cell, return the number of
	   neighbors that are ALIVE

	   Use get_cell_state(x,y) */
	int i,j,alives=0;
	for(i=-1;i<2;++i){
		for(j=-1;j<2;++j){
			if(x+i<0 || y+j<0 || x+i>=get_world_width() || y+j>= get_world_height() || 
			(i==0 && j==0)) continue;
			if(get_cell_state(x+i,y+j)==ALIVE) ++alives;
		}
	}
	return alives;
}
