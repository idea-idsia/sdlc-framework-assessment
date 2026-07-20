# Prompt:

> ```
> Create a snake game in Python
> ## Requirements:
> ### Game Board:
> - Create a grid-based game board.
> - Define the dimensions of the grid (e.g., 10x10).
> - Display the grid on the screen.
> ### Snake Initialization:
> - Place the snake on the game board.
> - Define the initial length and starting position of the snake.
> - Choose a direction for the snake to start moving immediately, without user input (e.g., right).
> ### Snake Movement:
> - Implement arrow key controls for snake movement.
> - Ensure the snake moves continuously in the chosen direction.
> - Update the snake’s position on the grid.
> ### Food Generation:
> - Generate food at random positions on the game board.
> - Ensure food doesn’t appear on the snake’s body.
> ### Collision Handling:
> - Detect collisions between the snake and the game board boundaries.
> - Detect collisions between the snake’s head and its body.
> - Detect collisions between the snake’s head and the food.
> ### Snake Growth:
> - Increase the length of the snake when it consumes food, adding a new segment to the snake’s body.
> ### Score Display:
> - Implement a scoring system.
> - Display the current score on the screen.
> ### Game Over Condition:
> - Trigger a game over scenario when the snake collides with the boundaries.
> - Trigger a game over scenario when the snake collides with its own body.
> - Display a game over message.
> - Allow the player to restart the game.
> ### Graphics and User Interface:
> - Use graphics or ASCII characters to represent the snake and food.
> - Design a user-friendly interface with clear instructions.
> ### Animations and Effects:
> - Add animations for snake movement and growth.
> - Implement visual effects for collisions and food consumption.
> ```


# RQ1 – UC1 Results

**Performance of different LLMs without frameworks and combined with different frameworks (UC1).**  
Notation:  
- **CG (Y/N)**: Code Generated  
- **CE (Y/N)**: Code Executed  
- **RT**: Runtime (seconds)  
- **RM**: Requirements Met (out of 10)

| Scenario | CG | CE | RT (s) | RM |
|----------|----|----|--------|----|
| qwen_32b_q4 | Y | Y | 233.00 | 8 |
| qwen_32b_q4 + MetaGPT | Y | Y | 1361.28 | 4 |
| qwen_32b_q4 + ChatDev | Y | N | 10277.00 | 0 |
| qwen_32b_q4 + AgileCoder | Y | Y | 2641.00 | 8 |
| qwen_32b_q4 + HyperAgent | Y | Y | 161.97 | 1 |
| gemma_27b_fp16 | Y | Y | 866.00 | 9 |
| gemma_27b_fp16 + MetaGPT | Y | Y | 4739.48 | 0 |
| gemma_27b_fp16 + ChatDev | N | N | 20995.00 | 0 |
| gemma_27b_fp16 + AgileCoder | Y | Y | 4969.00 | 3 |
| gemma_27b_fp16 + HyperAgent | Y | N | 2168.33 | 0 |
| qwen2_7b_fp16 | Y | Y | 131.00 | 8 |
| qwen2_7b_fp16 + MetaGPT | Y | N | 719.93 | 0 |
| qwen2_7b_fp16 + ChatDev | N | N | 1911.00 | 0 |
| qwen2_7b_fp16 + AgileCoder | Y | N | 1636.00 | 0 |
| qwen2_7b_fp16 + HyperAgent | Y | Y | 93.14 | 1 |
| qwen2_7b_q4 | Y | N | 68.00 | 0 |
| qwen2_7b_q4 + MetaGPT | Y | Y | 356.07 | 0 |
| qwen2_7b_q4 + ChatDev | N | N | 851.00 | 0 |
| qwen2_7b_q4 + AgileCoder | Y | Y | 2541.00 | 2 |
| qwen2_7b_q4 + HyperAgent | Y | N | 91.91 | 0 |
| gpt_oss_20b (run 2) | Y | Y | 35.34 | 8 |
| gpt_oss_20b + MetaGPT | Y | Y | 561.67 | 8 |
| gpt_oss_20b + ChatDev | Y | Y | 306.00 | 10 |
| gpt_oss_20b + AgileCoder | Y | Y | 623.00 | 3 |
| gpt_oss_20b + HyperAgent | N | N | 18.09 | 0 |
| llama3_70b_q3 (run 2) | Y | Y | 254.76 | 9 |
| llama3_70b_q3 + MetaGPT | Y | Y | 2190.71 | 8 |
| llama3_70b_q3 + ChatDev | Y | Y | 3075.00 | 4 |
| llama3_70b_q3 + AgileCoder | Y | Y | 24000.00 | 0 |
| llama3_70b_q3 (run 3) + HyperAgent | Y | Y | 1994.17 | 8 |
| llama3_70b_q4 (run 3) | Y | Y | 257.88 | 9 |
| llama3_70b_q4 + MetaGPT | N | N | 2777.27 | 0 |
| llama3_70b_q4 + ChatDev | Y | Y | 3379.00 | 6 |
| llama3_70b_q4 + AgileCoder | Y | Y | 31906.00 | 6 |
| llama3_70b_q4 + HyperAgent | Y | Y | 779.40 | 0 |
| devstral_24b_fp16 | Y | Y | 440.00 | 7 |
| devstral_24b_fp16 + MetaGPT | Y | Y | 1400.02 | 8 |
| devstral_24b_fp16 + ChatDev | Y | N | 4506.00 | 0 |
| devstral_24b_fp16 + AgileCoder | Y | N | 1325.00 | 0 |
| devstral_24b_fp16 + HyperAgent | Y | N | 2649.08 | 0 |


# Qualitative evaluation - Objective metrics
Only models that produced executable code are reported

### MetaGPT

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M  | na   | 1/30; 1/50 | No | Yes | No  |
| gemma3_27b_it_fp16           | 0.06 | na         | No | Yes | No  |
| qwen2_5_7b_instruct_q4_K_M   | 0.06 | na         | No | Yes | No  |
| gpt_oss_20b                  | 0.42 | 1/12; 1/12 | No | No  | No  |
| llama3_3_70b_instruct_q3_K_M | 2.73 | 1/30; 1/40 | No | Yes | Yes |
| devstral_24b_small_2505_fp16 | 4.8  | 1/48; 1/68 | No | Yes | No  |

### ChatDev

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| gpt_oss_20b                  | 2.29 | 1/20; 1/20 | Yes | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M | 2.67 | 1/30; 1/40 | No  | Yes | No  |
| llama3_3_70b_instruct_q4_K_M | 0.49 | 1/30; 1/40 | Yes | Yes | Yes |

### AgileCoder

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M  | 3.84 | 1/60; 1/70 | No | Yes | No  |
| gemma3_27b_it_fp16           | 0.95 | 1/20; 1/20 | No | Yes | No  |
| codellama_7b_instruct_fp16   | 0.15 | na         | No | Yes | No  |
| qwen2_5_7b_instruct_fp16     | 0.0  | na         | No | Yes | No  |
| qwen2_5_7b_instruct_q4_K_M   | 0.0  | 1/10; 1/10 | No | Yes | No  |
| gpt_oss_20b                  | 0.0  | 1/10; 1/10 | No | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M | na   | na         | No | Yes | No  |
| llama3_3_70b_instruct_q4_K_M | ?    | 1/30; 1/40 | No | Yes | No  |

### HyperAgent

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M        | 0.36 | 1/30; 1/40 | No  | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M       | 0.85 | 1/20; 1/20 | Yes | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M_run_2 | 1.72 | 1/30; 1/30 | Yes | Yes | No  |
| llama3_3_70b_instruct_q3_K_M_run_3 | 2.72 | 1/30; 1/40 | Yes | Yes | No  |
| llama3_3_70b_instruct_q4_K_M       | 0.0  | na         | No  | Yes | Yes |

### No-framework

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M               | 2.10 | 1/40; 1/60 | No  | Yes | No  |
| gemma3_27b_it_fp16                        | 1.37 | 1/20; 1/30 | Yes | Yes | No  |
| qwen2_5_7b_instruct_fp16                  | 2.1  | 1/40; 1/60 | No  | Yes | No  |
| qwen2_5_7b_instruct_q4_K_M                | na   | 1/20; 1/20 | No  | Yes | No  |
| gpt_oss_20b_run_2                         | 0.48 | 1/10; 1/10 | No  | Yes | Yes |
| deepseek_coder_v2_16b_lite_instruct_fp16  | 0.91 | 1/10; 1/10 | No  | Yes | No  |
| gemma3_27b_it_q4_K_M                      | 1.07 | 1/20; 1/20 | Yes | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M              | 2.81 | 1/30; 1/40 | Yes | Yes | No  |
| llama3_3_70b_instruct_q3_K_M_run_2        | 1.61 | 1/30; 1/20 | Yes | Yes | Yes |
| llama3_3_70b_instruct_q4_K_M              | 2.10 | 1/25; 1/35 | No  | Yes | No  |
| llama3_3_70b_instruct_q4_K_M_run_3        | 2.80 | 1/30; 1/40 | Yes | Yes | No  |
| nemotron_70b_instruct_q8_0                | 0.81 | 1/10; 1/10 | Yes | Yes | No  |
| qwen2_5_32b_instruct_fp16                 | na   | 1/40; 1/50 | Yes | Yes | No  |
| qwen2_5_coder_32b_instruct_fp16           | 2.21 | 1/40; 1/50 | No  | Yes | No  |
| qwen2_5_coder_32b_instruct_q4_K_M         | na   | 1/40; 1/50 | No  | Yes | No  |
### MetaGPT

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M  | na   | 1/30; 1/50 | No | Yes | No  |
| gemma3_27b_it_fp16           | 0.06 | na         | No | Yes | No  |
| qwen2_5_7b_instruct_q4_K_M   | 0.06 | na         | No | Yes | No  |
| gpt_oss_20b                  | 0.42 | 1/12; 1/12 | No | No  | No  |
| llama3_3_70b_instruct_q3_K_M | 2.73 | 1/30; 1/40 | No | Yes | Yes |
| devstral_24b_small_2505_fp16 | 4.8  | 1/48; 1/68 | No | Yes | No  |

### ChatDev

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| gpt_oss_20b                  | 2.29 | 1/20; 1/20 | Yes | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M | 2.67 | 1/30; 1/40 | No  | Yes | No  |
| llama3_3_70b_instruct_q4_K_M | 0.49 | 1/30; 1/40 | Yes | Yes | Yes |

### AgileCoder

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M  | 3.84 | 1/60; 1/70 | No | Yes | No  |
| gemma3_27b_it_fp16           | 0.95 | 1/20; 1/20 | No | Yes | No  |
| codellama_7b_instruct_fp16   | 0.15 | na         | No | Yes | No  |
| qwen2_5_7b_instruct_fp16     | 0.0  | na         | No | Yes | No  |
| qwen2_5_7b_instruct_q4_K_M   | 0.0  | 1/10; 1/10 | No | Yes | No  |
| gpt_oss_20b                  | 0.0  | 1/10; 1/10 | No | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M | na   | na         | No | Yes | No  |
| llama3_3_70b_instruct_q4_K_M | ?    | 1/30; 1/40 | No | Yes | No  |

### HyperAgent

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M        | 0.36 | 1/30; 1/40 | No  | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M       | 0.85 | 1/20; 1/20 | Yes | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M_run_2 | 1.72 | 1/30; 1/30 | Yes | Yes | No  |
| llama3_3_70b_instruct_q3_K_M_run_3 | 2.72 | 1/30; 1/40 | Yes | Yes | No  |
| llama3_3_70b_instruct_q4_K_M       | 0.0  | na         | No  | Yes | Yes |

### No-framework

| LLM | Time to Death (s) | Snake/board ratio | System status clear | GUI | Grid rendered |
|---|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M               | 2.10 | 1/40; 1/60 | No  | Yes | No  |
| gemma3_27b_it_fp16                        | 1.37 | 1/20; 1/30 | Yes | Yes | No  |
| qwen2_5_7b_instruct_fp16                  | 2.1  | 1/40; 1/60 | No  | Yes | No  |
| qwen2_5_7b_instruct_q4_K_M                | na   | 1/20; 1/20 | No  | Yes | No  |
| gpt_oss_20b_run_2                         | 0.48 | 1/10; 1/10 | No  | Yes | Yes |
| deepseek_coder_v2_16b_lite_instruct_fp16  | 0.91 | 1/10; 1/10 | No  | Yes | No  |
| gemma3_27b_it_q4_K_M                      | 1.07 | 1/20; 1/20 | Yes | Yes | Yes |
| llama3_3_70b_instruct_q3_K_M              | 2.81 | 1/30; 1/40 | Yes | Yes | No  |
| llama3_3_70b_instruct_q3_K_M_run_2        | 1.61 | 1/30; 1/20 | Yes | Yes | Yes |
| llama3_3_70b_instruct_q4_K_M              | 2.10 | 1/25; 1/35 | No  | Yes | No  |
| llama3_3_70b_instruct_q4_K_M_run_3        | 2.80 | 1/30; 1/40 | Yes | Yes | No  |
| nemotron_70b_instruct_q8_0                | 0.81 | 1/10; 1/10 | Yes | Yes | No  |
| qwen2_5_32b_instruct_fp16                 | na   | 1/40; 1/50 | Yes | Yes | No  |
| qwen2_5_coder_32b_instruct_fp16           | 2.21 | 1/40; 1/50 | No  | Yes | No  |
| qwen2_5_coder_32b_instruct_q4_K_M         | na   | 1/40; 1/50 | No  | Yes | No  |


# Qualitative evaluation - Subjective metrics
## (Score: Playability - Entertainment - Aesthetics)
Only models that produced executable code are reported

### MetaGPT

| LLM | Annotator | Playability | Entertainment | Aesthetics |
|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M  | Annotator 1 | 1 | 1 | 2 |
|                              | Annotator 2 | 1 | 1 | 2 |
|                              | Annotator 3 | 1 | 2 | 2 |
|                              | Annotator 4 | 1 | 1 | 2 |
| gemma3_27b_it_fp16           | Annotator 1 | 1 | 1 | 1 |
|                              | Annotator 2 | 1 | 1 | 1 |
|                              | Annotator 3 | 1 | 1 | 1 |
|                              | Annotator 4 | 1 | 1 | 1 |
| qwen2_5_7b_instruct_q4_K_M   | Annotator 1 | 1 | 1 | 1 |
|                              | Annotator 2 | 1 | 1 | 1 |
|                              | Annotator 3 | 1 | 1 | 1 |
|                              | Annotator 4 | 1 | 1 | 1 |
| gpt_oss_20b                  | Annotator 1 | 1 | 1 | 1 |
|                              | Annotator 2 | 1 | 2 | 1 |
|                              | Annotator 3 | 1 | 1 | 1 |
|                              | Annotator 4 | 1 | 1 | 2 |
| llama3_3_70b_instruct_q3_K_M | Annotator 1 | 3 | 3 | 3 |
|                              | Annotator 2 | 3 | 2 | 3 |
|                              | Annotator 3 | 3 | 3 | 3 |
|                              | Annotator 4 | 2 | 2 | 2 |
| devstral_24b_small_2505_fp16 | Annotator 1 | 3 | 2 | 2 |
|                              | Annotator 2 | 3 | 2 | 2 |
|                              | Annotator 3 | 3 | 2 | 2 |
|                              | Annotator 4 | 3 | 2 | 2 |

### ChatDev

| LLM | Annotator | Playability | Entertainment | Aesthetics |
|---|---|---|---|---|
| gpt_oss_20b                  | Annotator 1 | 2 | 2 | 3 |
|                              | Annotator 2 | 2 | 2 | 3 |
|                              | Annotator 3 | 3 | 2 | 2 |
|                              | Annotator 4 | 2 | 2 | 2 |
| llama3_3_70b_instruct_q3_K_M | Annotator 1 | 1 | 1 | 2 |
|                              | Annotator 2 | 1 | 1 | 2 |
|                              | Annotator 3 | 1 | 1 | 1 |
|                              | Annotator 4 | 1 | 1 | 1 |
| llama3_3_70b_instruct_q4_K_M | Annotator 1 | 1 | 1 | 2 |
|                              | Annotator 2 | 1 | 1 | 1 |
|                              | Annotator 3 | 1 | 1 | 3 |
|                              | Annotator 4 | 1 | 1 | 2 |

### AgileCoder

| LLM | Annotator | Playability | Entertainment | Aesthetics |
|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M  | Annotator 1 | 2 | 1 | 2 |
|                              | Annotator 2 | 3 | 1 | 2 |
|                              | Annotator 3 | 3 | 2 | 2 |
|                              | Annotator 4 | 2 | 2 | 2 |
| gemma3_27b_it_fp16           | Annotator 1 | 1 | 1 | 2 |
|                              | Annotator 2 | 1 | 1 | 2 |
|                              | Annotator 3 | 1 | 1 | 2 |
|                              | Annotator 4 | 1 | 1 | 2 |
| gpt_oss_20b                  | Annotator 1 | 1 | 1 | 2 |
|                              | Annotator 2 | 1 | 1 | 2 |
|                              | Annotator 3 | 1 | 1 | 3 |
|                              | Annotator 4 | 1 | 2 | 1 |
| llama3_3_70b_instruct_q4_K_M | Annotator 1 | 2 | 1 | 2 |
|                              | Annotator 2 | 2 | 1 | 2 |
|                              | Annotator 3 | 2 | 2 | 2 |
|                              | Annotator 4 | 1 | 1 | 2 |

### HyperAgent

| LLM | Annotator | Playability | Entertainment | Aesthetics |
|---|---|---|---|---|
| llama3_3_70b_instruct_q3_K_M       | Annotator 1 | 3 | 2 | 3 |
|                                    | Annotator 2 | 3 | 3 | 3 |
|                                    | Annotator 3 | 3 | 3 | 3 |
|                                    | Annotator 4 | 2 | 2 | 2 |
| llama3_3_70b_instruct_q3_K_M_run_2 | Annotator 1 | 3 | 3 | 2 |
|                                    | Annotator 2 | 3 | 2 | 2 |
|                                    | Annotator 3 | 3 | 3 | 2 |
|                                    | Annotator 4 | 2 | 2 | 1 |
| llama3_3_70b_instruct_q3_K_M_run_3 | Annotator 1 | 3 | 2 | 2 |
|                                    | Annotator 2 | 3 | 2 | 2 |
|                                    | Annotator 3 | 3 | 3 | 2 |
|                                    | Annotator 4 | 2 | 2 | 1 |

### No-framework

| LLM | Annotator | Playability | Entertainment | Aesthetics |
|---|---|---|---|---|
| qwen2_5_32b_instruct_q4_K_M               | Annotator 1 | 2 | 1 | 2 |
|                                           | Annotator 2 | 3 | 2 | 2 |
|                                           | Annotator 3 | 3 | 2 | 2 |
|                                           | Annotator 4 | 2 | 1 | 1 |
| gemma3_27b_it_fp16                        | Annotator 1 | 3 | 2 | 2 |
|                                           | Annotator 2 | 3 | 2 | 2 |
|                                           | Annotator 3 | 3 | 3 | 2 |
|                                           | Annotator 4 | 2 | 2 | 2 |
| qwen2_5_7b_instruct_fp16                  | Annotator 1 | 3 | 2 | 1 |
|                                           | Annotator 2 | 3 | 2 | 2 |
|                                           | Annotator 3 | 3 | 2 | 2 |
|                                           | Annotator 4 | 2 | 1 | 1 |
| gpt_oss_20b_run_2                         | Annotator 1 | 2 | 1 | 2 |
|                                           | Annotator 2 | 2 | 2 | 2 |
|                                           | Annotator 3 | 2 | 2 | 3 |
|                                           | Annotator 4 | 2 | 1 | 1 |
| deepseek_coder_v2_16b_lite_instruct_fp16  | Annotator 1 | 1 | 1 | 1 |
|                                           | Annotator 2 | 1 | 1 | 1 |
|                                           | Annotator 3 | 1 | 1 | 1 |
|                                           | Annotator 4 | 1 | 1 | 1 |
| gemma3_27b_it_q4_K_M                      | Annotator 1 | 3 | 2 | 3 |
|                                           | Annotator 2 | 3 | 3 | 3 |
|                                           | Annotator 3 | 3 | 3 | 2 |
|                                           | Annotator 4 | 2 | 2 | 2 |
| llama3_3_70b_instruct_q3_K_M              | Annotator 1 | 3 | 3 | 2 |
|                                           | Annotator 2 | 3 | 2 | 2 |
|                                           | Annotator 3 | 3 | 3 | 2 |
|                                           | Annotator 4 | 2 | 2 | 2 |
| llama3_3_70b_instruct_q3_K_M_run_2        | Annotator 1 | 3 | 3 | 3 |
|                                           | Annotator 2 | 3 | 3 | 3 |
|                                           | Annotator 3 | 3 | 2 | 2 |
|                                           | Annotator 4 | 2 | 2 | 2 |
| llama3_3_70b_instruct_q4_K_M              | Annotator 1 | 1 | 1 | 2 |
|                                           | Annotator 2 | 1 | 1 | 2 |
|                                           | Annotator 3 | 1 | 1 | 2 |
|                                           | Annotator 4 | 1 | 1 | 2 |
| llama3_3_70b_instruct_q4_K_M_run_3        | Annotator 1 | 2 | 2 | 2 |
|                                           | Annotator 2 | 3 | 3 | 2 |
|                                           | Annotator 3 | 3 | 3 | 2 |
|                                           | Annotator 4 | 2 | 2 | 2 |
| nemotron_70b_instruct_q8_0                | Annotator 1 | 1 | 1 | 2 |
|                                           | Annotator 2 | 2 | 1 | 2 |
|                                           | Annotator 3 | 2 | 1 | 2 |
|                                           | Annotator 4 | 1 | 1 | 1 |
| qwen2_5_32b_instruct_fp16                 | Annotator 1 | 2 | 2 | 1 |
|                                           | Annotator 2 | 2 | 2 | 2 |
|                                           | Annotator 3 | 3 | 3 | 2 |
|                                           | Annotator 4 | 2 | 2 | 1 |
| qwen2_5_coder_32b_instruct_fp16           | Annotator 1 | 3 | 2 | 1 |
|                                           | Annotator 2 | 3 | 2 | 2 |
|                                           | Annotator 3 | 3 | 2 | 2 |
|                                           | Annotator 4 | 2 | 1 | 1 |
| qwen2_5_coder_32b_instruct_q4_K_M         | Annotator 1 | 3 | 2 | 1 |
|                                           | Annotator 2 | 2 | 2 | 2 |
|                                           | Annotator 3 | 3 | 2 | 2 |
|                                           | Annotator 4 | 2 | 1 | 1 |