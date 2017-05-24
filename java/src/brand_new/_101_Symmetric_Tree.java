package brand_new;

public class _101_Symmetric_Tree {
	public boolean isSymmetric(TreeNode root) {
		if (root == null)
			return true;
		return isSymmetric(root.left, root.right);
	}

	public boolean isSymmetric(TreeNode node1, TreeNode node2) {
		if (node1 == null && node2 == null)
			return true;
		if (node1 == null || node2 == null)
			return false;

		if (node1.val != node2.val)
			return false;

		return isSymmetric(node1.left, node2.right)
				&& isSymmetric(node1.right, node2.left);

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
