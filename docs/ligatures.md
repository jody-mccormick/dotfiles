# Programming Ligatures Showcase

Ligature-friendly fonts (e.g., Fira Code, JetBrains Mono, Cascadia Code, Hasklig, Monaspace) render common operator sequences as beautiful combined glyphs. This page demonstrates typical sequences across languages to preview how they look in your editor/terminal.

Tip: Ensure your editor/terminal has font ligatures enabled for your chosen font.

- VS Code: Settings → “Font Ligatures” → true
- JetBrains IDEs: Preferences → Editor → Font → Enable font ligatures
- iTerm2/Terminal: Profiles → Text → Use a font with ligatures

---

## JavaScript / TypeScript
```ts
// Comparisons
if (a <= b && b >= c) {}
if (x === y || x !== z) {}

// Arrow functions and nullish/optional
const add = (a: number, b: number) => a + b; // =>
const name = user?.profile?.name ?? "unknown"; // ?.  ??

// Pipes, bitwise, shifts
value ||= 0; // ||=  (logical-or assign)
flags &= ~MASK; // &=  ~
let shifted = n >> 2; // >>

// Ranges and spreads
const arr = [1, 2, 3, ...rest]; // ...

// Comments
// line comment
/* block comment */
```

## Python
```python
# Comparisons
if a <= b and b >= c:
    pass
if x == y or x != z:
    pass

# Walrus and annotations (no special ligature, but shown for context)
if (n := len(items)) > 0:  # :=
    print(n)

# Arrows in type hints (some fonts stylize ->)
def add(a: int, b: int) -> int:  # ->
    return a + b
```

## Go
```go
// Comparisons and assignment
if a <= b && b >= c {}
if x == y || x != z {}

// Short declaration and pointers
v := 42       // :=
var p *int    // *

// Maps and slices
m := map[string]int{"a": 1}
s := []int{1, 2, 3}

// Function literal
f := func(a, b int) int { return a + b } // :=  {}
```

## Rust
```rust
// Comparisons and logical ops
if a <= b && b >= c {}
if x == y || x != z {}

// Closures and turbofish
let add = |a: i32, b: i32| a + b; // | |  =>-like shape in some fonts
let v = Vec::<i32>::new();        // ::

// Ranges
for i in 0..=10 { /* ..= */ }

// References and arrows in comments
let r: &i32 = &x; // &  &
```

## C / C++
```cpp
// Comparisons and logical ops
if (a <= b && b >= c) {}
if (x == y || x != z) {}

// Pointers, arrows, shifts
ptr->field = 1;   // ->
int m = n << 1;   // <<

// Namespaces
std::vector<int> v; // ::

// Comments
// line comment
/* block comment */
```

## Java
```java
// Comparisons and logical ops
if (a <= b && b >= c) {}
if (x == y || x != z) {}

// Lambdas and method refs
Function<Integer,Integer> inc = x -> x + 1; // ->
list.forEach(System.out::println);          // ::
```

## C#
```csharp
// Comparisons and logical ops
if (a <= b && b >= c) {}
if (x == y || x != z) {}

// Lambdas and null-coalescing
Func<int,int> inc = x => x + 1; // =>
var name = person?.Name ?? "unknown"; // ?.  ??
```

## Kotlin
```kotlin
// Comparisons and logical ops
if (a <= b && b >= c) {}
if (x == y || x != z) {}

// Lambdas and ranges
val inc: (Int) -> Int = { x -> x + 1 } // ->
for (i in 0..10) { } // ..

// Safe calls and Elvis
val name = user?.profile?.name ?: "unknown" // ?.  ?:
```

## Swift
```swift
// Comparisons and logical ops
if a <= b && b >= c {}
if x == y || x != z {}

// Closures and ranges
let inc: (Int) -> Int = { x in x + 1 } // ->
for i in 0...10 { } // ...
```

## Haskell
```haskell
-- Comparisons and logical-ish operators
if a <= b then () else ()

-- Function composition and arrows
f = g . h         -- .
foo :: Int -> Int -- ::  ->

-- Lambda
\x -> x + 1      -- \
```

## Ruby
```ruby
# Comparisons and logical ops
if a <= b && b >= c; end
if x == y || x != z; end

# Hash rockets and symbols
h = { :a => 1, :b => 2 } # =>
```

## Elixir
```elixir
# Comparisons and logical ops
if a <= b and b >= c, do: :ok
if x == y or x != z, do: :ok

# Pipe and capture
result = data |> Enum.map(& &1) # |>
```

## Bash
```bash
# Comparisons
[ $a -le $b ] && [ $b -ge $c ]
[ "$x" = "$y" ] || [ "$x" != "$z" ]

# Redirection and pipes
cat file.txt | grep foo >> out.log 2>&1  # |  >>  2>&1
```

---

## Fonts that support programming ligatures
- Fira Code
- JetBrains Mono
- Cascadia Code
- Hasklig
- Monaspace

If a sequence does not render as a single glyph, your font may not support it or ligatures may be disabled in your editor.
