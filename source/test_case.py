import unittest
import const
import case


class test_case(unittest.TestCase):
    def setUp(self):
        self.case_par_defaut = case.Case()
        self.case_mur = case.Case(True)
        self.case_mur_pA = case.Case(True, pacmans_presents={"A"})
        self.case_pA = case.Case(False, const.AUCUN, {"A"})
        self.case_fc = case.Case(False, const.AUCUN, None, {"c"})
        self.case_pB_fab = case.Case(False, const.AUCUN, {"B"}, {"a", "b"})
        self.case_oGlouton = case.Case(False, const.GLOUTON)
        self.case_pB_oPassemuraille = case.Case(
            False, const.PASSEMURAILLE, {"B"})
        self.case_pAB_fc_oValeur = case.Case(
            False, const.VALEUR, {"A", "B"}, {"c"})

    def test_est_mur(self):
        self.assertFalse(case.est_mur(self.case_par_defaut))
        self.assertFalse(case.est_mur(self.case_pA))
        self.assertFalse(case.est_mur(self.case_fc))
        self.assertFalse(case.est_mur(self.case_pB_fab))
        self.assertFalse(case.est_mur(self.case_oGlouton))
        self.assertFalse(case.est_mur(self.case_pB_oPassemuraille))
        self.assertFalse(case.est_mur(self.case_pAB_fc_oValeur))

        self.assertTrue(case.est_mur(self.case_mur))
        self.assertTrue(case.est_mur(self.case_mur_pA))

    def test_get_objet(self):
        self.assertEqual(case.get_objet(self.case_par_defaut), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_pA), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_fc), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_pB_fab), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_oGlouton), const.GLOUTON)
        self.assertEqual(case.get_objet(
            self.case_pB_oPassemuraille), const.PASSEMURAILLE)
        self.assertEqual(case.get_objet(
            self.case_pAB_fc_oValeur), const.VALEUR)
        self.assertEqual(case.get_objet(self.case_mur), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_mur_pA), const.AUCUN)

    def test_get_pacmans(self):
        self.assertEqual(case.get_pacmans(self.case_par_defaut), set())
        self.assertEqual(case.get_pacmans(self.case_pA), {"A"})
        self.assertEqual(case.get_pacmans(self.case_fc), set())
        self.assertEqual(case.get_pacmans(self.case_pB_fab), {"B"})
        self.assertEqual(case.get_pacmans(self.case_oGlouton), set())
        self.assertEqual(case.get_pacmans(self.case_pB_oPassemuraille), {"B"})
        self.assertEqual(case.get_pacmans(
            self.case_pAB_fc_oValeur), {"A", "B"})
        self.assertEqual(case.get_pacmans(self.case_mur), set())
        self.assertEqual(case.get_pacmans(self.case_mur_pA), {"A"})

    def test_get_fantomes(self):
        self.assertEqual(case.get_fantomes(self.case_par_defaut), set())
        self.assertEqual(case.get_fantomes(self.case_pA), set())
        self.assertEqual(case.get_fantomes(self.case_fc), {"c"})
        self.assertEqual(case.get_fantomes(self.case_pB_fab), {"a", "b"})
        self.assertEqual(case.get_fantomes(self.case_oGlouton), set())
        self.assertEqual(case.get_fantomes(self.case_pB_oPassemuraille), set())
        self.assertEqual(case.get_fantomes(self.case_pAB_fc_oValeur), {"c"})
        self.assertEqual(case.get_fantomes(self.case_mur), set())
        self.assertEqual(case.get_fantomes(self.case_mur_pA), set())

    def test_get_nb_pacmans(self):
        self.assertEqual(case.get_nb_pacmans(self.case_par_defaut), 0)
        self.assertEqual(case.get_nb_pacmans(self.case_pA), 1)
        self.assertEqual(case.get_nb_pacmans(self.case_fc), 0)
        self.assertEqual(case.get_nb_pacmans(self.case_pB_fab), 1)
        self.assertEqual(case.get_nb_pacmans(self.case_oGlouton), 0)
        self.assertEqual(case.get_nb_pacmans(self.case_pB_oPassemuraille), 1)
        self.assertEqual(case.get_nb_pacmans(self.case_pAB_fc_oValeur), 2)
        self.assertEqual(case.get_nb_pacmans(self.case_mur), 0)
        self.assertEqual(case.get_nb_pacmans(self.case_mur_pA), 1)

    def test_get_nb_fantomes(self):
        self.assertEqual(case.get_nb_fantomes(self.case_par_defaut), 0)
        self.assertEqual(case.get_nb_fantomes(self.case_pA), 0)
        self.assertEqual(case.get_nb_fantomes(self.case_fc), 1)
        self.assertEqual(case.get_nb_fantomes(self.case_pB_fab), 2)
        self.assertEqual(case.get_nb_fantomes(self.case_oGlouton), 0)
        self.assertEqual(case.get_nb_fantomes(self.case_pB_oPassemuraille), 0)
        self.assertEqual(case.get_nb_fantomes(self.case_pAB_fc_oValeur), 1)
        self.assertEqual(case.get_nb_fantomes(self.case_mur), 0)
        self.assertEqual(case.get_nb_fantomes(self.case_mur_pA), 0)

    def test_get_objet(self):
        self.assertEqual(case.get_objet(self.case_par_defaut), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_pA), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_fc), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_pB_fab), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_oGlouton), const.GLOUTON)
        self.assertEqual(case.get_objet(
            self.case_pB_oPassemuraille), const.PASSEMURAILLE)
        self.assertEqual(case.get_objet(
            self.case_pAB_fc_oValeur), const.VALEUR)
        self.assertEqual(case.get_objet(self.case_mur), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_mur_pA), const.AUCUN)

    def test_poser_objet(self):
        case.poser_objet(self.case_par_defaut, const.GLOUTON)
        self.assertEqual(case.get_objet(self.case_par_defaut), const.GLOUTON)
        case.poser_objet(self.case_pA, const.VALEUR)
        self.assertEqual(case.get_objet(self.case_pA), const.VALEUR)
        case.poser_objet(self.case_fc, const.VITAMINE)
        self.assertEqual(case.get_objet(self.case_fc), const.VITAMINE)
        case.poser_objet(self.case_oGlouton, const.AUCUN)
        self.assertEqual(case.get_objet(self.case_oGlouton), const.AUCUN)
        case.poser_objet(self.case_pB_fab, const.IMMOBILITE)
        self.assertEqual(case.get_objet(self.case_pB_fab), const.IMMOBILITE)
        case.poser_objet(self.case_pB_oPassemuraille, const.IMMOBILITE)
        self.assertEqual(case.get_objet(
            self.case_pB_oPassemuraille), const.IMMOBILITE)
        case.poser_objet(self.case_pAB_fc_oValeur, const.GLOUTON)
        self.assertEqual(case.get_objet(
            self.case_pAB_fc_oValeur), const.GLOUTON)
        case.poser_objet(self.case_mur, const.VALEUR)
        self.assertEqual(case.get_objet(self.case_mur), const.AUCUN)
        case.poser_objet(self.case_mur_pA, const.GLOUTON)
        self.assertEqual(case.get_objet(self.case_mur_pA), const.AUCUN)

    def test_prendre_objet(self):
        self.assertEqual(case.prendre_objet(self.case_par_defaut), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_par_defaut), const.AUCUN)
        self.assertEqual(case.prendre_objet(self.case_pA), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_pA), const.AUCUN)
        self.assertEqual(case.prendre_objet(self.case_fc), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_fc), const.AUCUN)
        self.assertEqual(case.prendre_objet(self.case_oGlouton), const.GLOUTON)
        self.assertEqual(case.get_objet(self.case_oGlouton), const.AUCUN)
        self.assertEqual(case.prendre_objet(self.case_pB_fab), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_pB_fab), const.AUCUN)
        self.assertEqual(case.prendre_objet(
            self.case_pB_oPassemuraille), const.PASSEMURAILLE)
        self.assertEqual(case.get_objet(
            self.case_pB_oPassemuraille), const.AUCUN)
        self.assertEqual(case.prendre_objet(
            self.case_pAB_fc_oValeur), const.VALEUR)
        self.assertEqual(case.get_objet(self.case_pAB_fc_oValeur), const.AUCUN)
        self.assertEqual(case.prendre_objet(self.case_mur), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_mur), const.AUCUN)
        self.assertEqual(case.prendre_objet(self.case_mur_pA), const.AUCUN)
        self.assertEqual(case.get_objet(self.case_mur_pA), const.AUCUN)

    def test_poser_pacman(self):
        case.poser_pacman(self.case_par_defaut, 'A')
        self.assertEqual(case.get_pacmans(self.case_par_defaut), {"A"})
        case.poser_pacman(self.case_pA, 'B')
        self.assertEqual(case.get_pacmans(self.case_pA), {"A", "B"})
        case.poser_pacman(self.case_fc, 'A')
        self.assertEqual(case.get_pacmans(self.case_fc), {'A'})
        case.poser_pacman(self.case_oGlouton, 'C')
        self.assertEqual(case.get_pacmans(self.case_oGlouton), {'C'})
        case.poser_pacman(self.case_pB_oPassemuraille, 'B')
        self.assertEqual(case.get_pacmans(self.case_pB_oPassemuraille), {'B'})
        case.poser_pacman(self.case_pB_fab, 'C')
        self.assertEqual(case.get_pacmans(self.case_pB_fab), {'B', 'C'})
        case.poser_pacman(self.case_pAB_fc_oValeur, 'C')
        self.assertEqual(case.get_pacmans(
            self.case_pAB_fc_oValeur), {'A', 'B', 'C'})
        case.poser_pacman(self.case_mur, 'C')
        self.assertEqual(case.get_pacmans(self.case_mur), {'C'})
        case.poser_pacman(self.case_mur_pA, 'A')
        self.assertEqual(case.get_pacmans(self.case_mur_pA), {'A'})

    def test_poser_fantome(self):
        case.poser_fantome(self.case_par_defaut, 'a')
        self.assertEqual(case.get_fantomes(self.case_par_defaut), {"a"})
        case.poser_fantome(self.case_pA, 'b')
        self.assertEqual(case.get_fantomes(self.case_pA), {"b"})
        case.poser_fantome(self.case_fc, 'a')
        self.assertEqual(case.get_fantomes(self.case_fc), {'a', 'c'})
        case.poser_fantome(self.case_oGlouton, 'b')
        self.assertEqual(case.get_fantomes(self.case_oGlouton), {'b'})
        case.poser_fantome(self.case_pB_oPassemuraille, 'a')
        self.assertEqual(case.get_fantomes(self.case_pB_oPassemuraille), {'a'})
        case.poser_fantome(self.case_pB_fab, 'c')
        self.assertEqual(case.get_fantomes(self.case_pB_fab), {'a', 'b', 'c'})
        case.poser_fantome(self.case_pAB_fc_oValeur, 'c')
        self.assertEqual(case.get_fantomes(self.case_pAB_fc_oValeur), {'c'})
        case.poser_fantome(self.case_mur, 'c')
        self.assertEqual(case.get_fantomes(self.case_mur), set())
        case.poser_fantome(self.case_mur_pA, 'b')
        self.assertEqual(case.get_fantomes(self.case_mur_pA), set())

    def test_prendre_pacman(self):
        self.assertFalse(case.prendre_pacman(self.case_par_defaut, 'A'))
        self.assertEqual(case.get_pacmans(self.case_par_defaut), set())
        self.assertTrue(case.prendre_pacman(self.case_pA, 'A'))
        self.assertEqual(case.get_pacmans(self.case_pA), set())
        self.assertFalse(case.prendre_pacman(self.case_fc, 'C'))
        self.assertEqual(case.get_pacmans(self.case_fc), set())
        self.assertFalse(case.prendre_pacman(self.case_oGlouton, 'A'))
        self.assertEqual(case.get_pacmans(self.case_oGlouton), set())
        self.assertTrue(case.prendre_pacman(self.case_pB_oPassemuraille, 'B'))
        self.assertEqual(case.get_pacmans(self.case_pB_oPassemuraille), set())
        self.assertFalse(case.prendre_pacman(self.case_pB_fab, 'A'))
        self.assertEqual(case.get_pacmans(self.case_pB_fab), {'B'})
        self.assertTrue(case.prendre_pacman(self.case_pAB_fc_oValeur, 'A'))
        self.assertEqual(case.get_pacmans(self.case_pAB_fc_oValeur), {'B'})
        self.assertFalse(case.prendre_pacman(self.case_mur, 'B'))
        self.assertEqual(case.get_pacmans(self.case_mur), set())
        self.assertTrue(case.prendre_pacman(self.case_mur_pA, 'A'))
        self.assertEqual(case.get_pacmans(self.case_mur_pA), set())

    def test_prendre_fantome(self):
        self.assertFalse(case.prendre_fantome(self.case_par_defaut, 'a'))
        self.assertEqual(case.get_fantomes(self.case_par_defaut), set())
        self.assertFalse(case.prendre_fantome(self.case_pA, 'b'))
        self.assertEqual(case.get_fantomes(self.case_pA), set())
        self.assertTrue(case.prendre_fantome(self.case_fc, 'c'))
        self.assertEqual(case.get_fantomes(self.case_fc), set())
        self.assertFalse(case.prendre_fantome(self.case_oGlouton, 'a'))
        self.assertEqual(case.get_fantomes(self.case_oGlouton), set())
        self.assertFalse(case.prendre_fantome(
            self.case_pB_oPassemuraille, 'b'))
        self.assertEqual(case.get_fantomes(self.case_pB_oPassemuraille), set())
        self.assertTrue(case.prendre_fantome(self.case_pB_fab, 'b'))
        self.assertEqual(case.get_fantomes(self.case_pB_fab), {'a'})
        self.assertTrue(case.prendre_fantome(self.case_pAB_fc_oValeur, 'c'))
        self.assertEqual(case.get_fantomes(self.case_pAB_fc_oValeur), set())
        self.assertFalse(case.prendre_fantome(self.case_mur, 'b'))
        self.assertEqual(case.get_fantomes(self.case_mur), set())
        self.assertFalse(case.prendre_fantome(self.case_mur_pA, 'a'))
        self.assertEqual(case.get_fantomes(self.case_mur_pA), set())


if __name__ == '__main__':
    unittest.main()
