### Repository Notes

Prompts and result tables can be found in the respective use case folders README files.

### Frameworks version used for tests:

**MetaGPT v0.8.2**:  
Repository: https://github.com/FoundationAgents/MetaGPT  
Commit hash number: _df9bc1858f7d396a7eef5d9718cab7587b63fd62_

For tests with **AgileCoder**, **ChatDev**, **HyperAgent**, apposite forks have been created to support local models served through Ollama:

**AgileCoder** (fork of https://github.com/FSoft-AI4Code/AgileCoder):  
Repository: https://github.com/MichelRosselli/AgileCoder/tree/feature/ollama-fix  
Commit hash number: _0dc96e6152527edfdc9622959bad12749bf3fc9f_

**ChatDev** (fork of https://github.com/skypu/ChatDev):  
Repository: https://github.com/MichelRosselli/ChatDev/tree/feature/ollama-fix  
Commit hash number: _f0b53a759d24b5f140cd4cdeb9a020542ef35547_

**HyperAgent** (fork of https://github.com/FSoft-AI4Code/HyperAgent):  
Repository: https://github.com/bossforcoding/HyperAgent/tree/ollama-implementation  
Commit hash number: _8b096e26ebdadcac505fb75f61ed268c900449bb_

### Qualitative evaluation

Results and images inserted in use cases README files. 

Qualitative evaluation metrics include Failure-related metrics, Usability and Appearance metrics. We aim at defining Usability and Appearance metrics in an objective way, however, in case of Snake game, we also have three (3) subjective metrics. Below are annotation guidelines that the annotators used to perform evaluation. 

#### Annotation Guidelines (co-created with GPT-4)

##### **🐍 Snake Game Annotation Guidelines**

**🎯 Goal**

Annotators evaluate a Snake game instance (video, playable build, or simulation) on three dimensions:

1. **Playability** – How well the game functions and can be played
2. **Entertainment** – How engaging or fun the experience is
3. **Aesthetics** – Visual and stylistic quality

Each dimension is rated on a **3-point Likert scale**:

- **1 = Poor**
- **2 = Average**
- **3 = Good**

##### **1. 🎮 Playability**

**Definition**

How functional, responsive, and playable the game is. Focus on **controls, mechanics, and technical performance**.

**What to Consider**

- Are controls responsive and predictable?
- Are there bugs, glitches, or crashes?
- Is the difficulty reasonable (not broken/unfair)?
- Is the current game state clear at any moment (score, game over, restart)?

**Scale**

**1 – Poor**

- Controls are laggy, broken, or unresponsive
- Game frequently glitches or crashes
- Core mechanics don’t work properly
- Unplayable or frustrating

**Example:**

- Snake passes through walls randomly
- Input delay makes turning impossible
- Game freezes after eating food


**2 – Average**

- Mostly playable, but with noticeable issues
- Minor bugs or inconsistencies
- Controls work but may feel slightly off

**Example:**

- Occasional lag or missed inputs
- Collision detection slightly inaccurate
- Game speed inconsistent


**3 – Good**

- Smooth, responsive, and reliable gameplay
- No major bugs or disruptions
- Clear and consistent mechanics

**Example:**

- Instant response to controls
- Accurate collision detection
- Stable performance throughout


##### **2. 🎉 Entertainment**

**Definition**

How engaging and enjoyable this specific implementation of Snake is, independent of the core gameplay mechanics. Focus on how the game’s execution, presentation, and added elements enhance or reduce enjoyment.

**What to Consider**

- Is there a sense of progression (e.g., speed scaling, score feedback)?
- Are there pacing choices made by the implementation, such as starting speed, speed-up curve, and optional difficulty settings?
- Is there challenge, excitement, reward, or variation?
- Would a user want to replay it?

**Scale**

**1 – Poor**

- Boring, repetitive, or frustrating
- No sense of progression or reward
- Feels tedious

**Example:**

- Snake moves too slowly with no challenge
- No increasing difficulty
- Gameplay feels monotonous


**2 – Average**

- Moderately engaging but not compelling
- Some fun elements, but limited depth

**Example:**

- Difficulty increases slightly over time
- Enjoyable for a short period
- Lacks variety or excitement

**3 – Good**

- Fun, engaging, and satisfying
- Encourages replayability
- Good balance of challenge and reward

**Example:**

- Speed increases in a satisfying way
- Player feels motivated to beat high score
- Gameplay creates tension and excitement


##### **3. 🎨 Aesthetics**

**Definition**

The visual appeal and overall presentation of the game.

**What to Consider**

- Clarity of visuals (easy to see snake, food, grid)
- Color choices and contrast
- Animations and smoothness
- Overall polish and style

**Scale**

**1 – Poor**

- Hard to see or understand visuals
- Cluttered, confusing, or unappealing
- No visual polish

**Example:**

- Snake blends into background
- Flickering or broken graphics
- Distracting or inconsistent colors

**2 – Average**

- Functional but plain visuals
- No major issues, but lacks polish

**Example:**

- Basic grid and snake design
- Clear but visually simple
- Minimal animation


**3 – Good**

- Visually appealing and polished
- Clear, consistent, and well-designed

**Example:**

- Smooth animations
- Good color contrast
- Clean UI with readable elements

