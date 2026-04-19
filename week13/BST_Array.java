import java.util.Arrays;

/**
 * A binary search tree of Strings backed by an array.
 *
 * Children positions are calculated using heap-style indexing:
 * left = 2 * parent + 1, right = 2 * parent + 2.
 */
public class BST_Array {
    private String[] tree;
    private int size;

    public BST_Array() {
        this(15);
    }

    public BST_Array(int initialCapacity) {
        if (initialCapacity <= 0) {
            throw new IllegalArgumentException("initialCapacity must be > 0");
        }
        tree = new String[initialCapacity];
        size = 0;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void insert(String value) {
        if (value == null) {
            throw new IllegalArgumentException("value cannot be null");
        }

        int index = 0;
        while (true) {
            ensureCapacity(index);

            if (tree[index] == null) {
                tree[index] = value;
                size++;
                return;
            }

            int cmp = value.compareTo(tree[index]);
            if (cmp == 0) {
                // Ignore duplicates for a set-like BST.
                return;
            } else if (cmp < 0) {
                index = leftChild(index);
            } else {
                index = rightChild(index);
            }
        }
    }

    public boolean contains(String value) {
        if (value == null) {
            return false;
        }

        int index = 0;
        while (index < tree.length && tree[index] != null) {
            int cmp = value.compareTo(tree[index]);
            if (cmp == 0) {
                return true;
            } else if (cmp < 0) {
                index = leftChild(index);
            } else {
                index = rightChild(index);
            }
        }
        return false;
    }

    public String getAtIndex(int index) {
        if (index < 0 || index >= tree.length) {
            throw new IndexOutOfBoundsException("index out of bounds: " + index);
        }
        return tree[index];
    }

    public int capacity() {
        return tree.length;
    }

    public String[] toArrayCopy() {
        return Arrays.copyOf(tree, tree.length);
    }

    @Override
    public String toString() {
        return Arrays.toString(tree);
    }

    private int leftChild(int parent) {
        return 2 * parent + 1;
    }

    private int rightChild(int parent) {
        return 2 * parent + 2;
    }

    private void ensureCapacity(int requiredIndex) {
        if (requiredIndex < tree.length) {
            return;
        }

        int newCapacity = tree.length;
        while (requiredIndex >= newCapacity) {
            newCapacity = newCapacity * 2 + 1;
        }
        tree = Arrays.copyOf(tree, newCapacity);
    }
}
