# arc-agi-attempts

In this repository I have code and brief explanations of my attempts at the ARC-AGI (2024) challenges.

## attempts

### 1. direct grid solution
- Located in: `direct-arc-solution.ipynb`
- Description: A pattern-matching approach where Claude analyzes the grids and makes direct predictions
- Key features:
    - Takes input/output grids displayed with emojis
    - Analyzes patterns through a thought process
    - Makes predictions without writing explicit code
    - Uses XML tags like `<thought>`, `<prediction>`, `<criticism>` to structure reasoning
    - Provides final predictions in emoji grid format

### 2. direct code solution
- Located in: `direct-code-arc-solution.ipynb`
- Description: A straightforward approach where Claude directly attempts to write code to solve the puzzle after analyzing the patterns
- Uses single-shot code generation with a customized prompt template
- Validates solutions against test cases

### 3. iterative code solution
- Located in: `iterative-code-arc-solution.ipynb`
- Description: An iterative approach where Claude gradually develops a solution through multiple steps
- Features:
  - Breaks down problem analysis into smaller steps
  - Maintains conversation history to build upon previous insights
  - Allows for refinement and correction of hypotheses

### 4. information bank based solution
- Located in: `bank-code-arc-solution.ipynb`
- Description: A structured approach that maintains a "bank" of collected knowledge and explorations
- Key components:
  - COLLECT phase: Gathers basic information about patterns
  - EXPLORE phase: Tests specific hypotheses about transformations
  - Uses systematic validation before proposing final solutions
- Benifit of this approch is, context lengths are shorted because we only use the information bank

## file structure

```
.
├── README.md
├── requirements.txt
├── puzzles/
│   └── arc-agi_test_challenges.json
├── prompts/
│   ├── direct_prompt.txt
│   ├── iterative_2_prompt.txt
│   └── bank_prompt.txt
└── attempts/
    └── [generated attempt logs]
```

## setup

1. Set up environment:
```bash
# Clone repository
git clone https://github.com/yourusername/arc-agi-attempts.git
cd arc-agi-attempts

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

2. Configure API key:
```bash
# Create .env file
echo "OPENROUTER_API_KEY=your_key_here" > .env
```