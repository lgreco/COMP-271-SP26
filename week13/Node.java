


public class Node {

    /** A node object for a binary tree. */

    private String content;   
    private Node left;
    private Node right;

    public Node(String data) {
        this.content = data;
        this.left = null;
        this.right = null;
    }

    public String getContent() {
        return content;
    }

    public Node getLeft() {
        return left;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    public Node getRight() {
        return right;
    }

    public void setRight(Node right) {
        this.right = right;
    }

    public boolean hasLeft() {
        return left != null;
    }

    public boolean hasRight() {
        return right != null;
    }

    public boolean isLeaf() {
        return !hasLeft() && !hasRight();
    }
}