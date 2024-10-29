// comptime forces inclusion. these imports
// are otherwise optimized out by the compiler.
comptime {
    _ = @import("problems/01/two_sum.zig");
    _ = @import("problems/02/valid_parentheses.zig");
    _ = @import("problems/03/merge_two_sorted_lists.zig");
    _ = @import("problems/15/ransom_note.zig");
    _ = @import("problems/59/water_container.zig");
}
